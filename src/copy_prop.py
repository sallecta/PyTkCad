# -*- coding: utf-8; -*-
from copy import copy
import param_edit
#КОПИРОВАНИЕ СВОЙСТВ
class Copy_prop:
    def __init__(self, par):
        self.par = par
        self.copy_prop()
        
    def copy_prop(self):
        self.par.standart_unbind()
        if self.par.collection and len(self.par.collection)==1:
            col = self.par.collection[0]
            self.par.kill()
            self.par.info.config(text = u'Escape - stop')
            self.par.dialog.config(text = u'Copying properties - object 2:')
            self.copy_prop3(col)
            self.par.c.bind('<Button-1>', self.copy_prop4)
            self.par.c.config(cursor = 'iron_cross')
        else:
            self.par.kill()
            self.par.info.config(text = u'Escape - stop')
            self.par.dialog.config(text = u'Copying properties - object 1:')
            self.par.c.bind('<Button-1>', self.copy_prop2)
        
        self.par.resFlag = True    
        #self.par.c.unbind_class(self.par.c,"<Motion>")
        self.par.unpriv = True
        self.par.c.unbind_class(self.par.master1,"<Return>")

    def copy_prop2(self, event = None):
        el = self.par.get_obj(event.x, event.y, 'all')
        if el:
            self.par.dialog.config(text = u'Copying properties - object 2:')
            self.par.c.bind('<Button-1>', self.copy_prop4)
            self.copy_prop3(el)
            self.par.c.config(cursor = 'iron_cross')
        
    def copy_prop3(self, col):
        self.par.prop = {}
        for p in self.par.ALLOBJECT[col]:
            if p in ('fill', 'width', 'stipple', 'factor_stip', 'size', 'sloy', 's', 'vr_s', 'vv_s', 'arrow_s', 'type_arrow', 's_s', 'w_text', 'font', 's_s_dim', 'w_text_dim', 'font_dim'):                       
                self.par.prop[p] = copy(self.par.ALLOBJECT[col][p])

    def copy_prop4(self, event):
        self.par.ex,self.par.ey = self.par.coordinator(self.par.ex,self.par.ey)
        self.par.ex2,self.par.ey2 = self.par.coordinator(self.par.ex2,self.par.ey2)
        self.par.set_coord()
        x = event.x
        y = event.y
        if self.par.rect:
            self.par.c.delete(self.par.rect)#Удалить прямоугольник выделения
            self.par.rect = None
            self.par.unpriv = True
            self.par.c.bind_class(self.par.c,"<Motion>", self.par.gpriv)
            x1 = min(self.par.rectx, self.par.rectx2)
            x2 = max(self.par.rectx, self.par.rectx2)
            y1 = min(self.par.recty, self.par.recty2)
            y2 = max(self.par.recty, self.par.recty2)
            c = self.par.c.find_overlapping(x1,y1,x2,y2)
            self.par.mass_collektor(c, 'select')
            if self.par.collection:
                
                param_edit.Param_edit(self.par, self.par.prop)
                self.par.sbros()
                self.par.changeFlag = True
                self.par.enumerator_p()
        else:
            el = self.par.get_obj(event.x, event.y, 'all')
            if el:
                self.par.collection = [el,]
                param_edit.Param_edit(self.par, self.par.prop)
                self.par.sbros()
                self.par.changeFlag = True
                self.par.enumerator_p()
            else:
                self.par.rectx = x
                self.par.recty = y
                self.par.unpriv = False
                self.par.c.bind_class(self.par.c, "<Motion>", self.par.resRect)
