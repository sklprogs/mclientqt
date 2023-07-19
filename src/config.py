#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import json
import jsonschema

from skl_shared_qt.localize import _
import skl_shared_qt.shared as sh

PRODUCT_LOW = 'mclient'


class Config:
    
    def __init__(self):
        self.Success = True
        self.pdefault = ''
        self.plocal = ''
        self.pschema = ''
        self.default = {}
        self.local = {}
        self.schema = {}
        self.new = {}
    
    def check_local(self):
        f = '[MClient] config.Config.check_local'
        if not self.Success:
            sh.com.cancel(f)
            return
        try:
            jsonschema.validate(self.local, self.schema)
        except jsonschema.exceptions.ValidationError as e:
            self.Success = False
            mes = _('Configuration file "{}" has values of a wrong type!\nFix, restore or delete this file.\n\nDetails:\n{}')
            mes = mes.format(self.plocal, e)
            sh.objs.get_mes(f, mes).show_error()
    
    def check_default(self):
        f = '[MClient] config.Config.check_default'
        if not self.Success:
            sh.com.cancel(f)
            return
        try:
            jsonschema.validate(self.default, self.schema)
        except jsonschema.exceptions.ValidationError as e:
            self.Success = False
            mes = _('Configuration file "{}" has values of a wrong type!\nFix or restore this file.\n\nDetails:\n{}')
            mes = mes.format(self.pdefault, e)
            sh.objs.get_mes(f, mes).show_error()
    
    def load_schema(self):
        f = '[MClient] config.Config.load_schema'
        if not self.Success:
            sh.com.cancel(f)
            return
        code = sh.ReadTextFile(self.pschema).get()
        if not code:
            self.Success = False
            sh.com.rep_out(f)
            return
        try:
            self.schema = json.loads(code)
        except Exception as e:
            self.Success = False
            sh.com.rep_third_party(f, e)
    
    def load_local(self):
        f = '[MClient] config.Config.load_local'
        if not self.Success:
            sh.com.cancel(f)
            return
        code = sh.ReadTextFile(self.plocal).get()
        if not code:
            self.Success = False
            sh.com.rep_out(f)
            return
        try:
            self.local = json.loads(code)
        except Exception as e:
            self.Success = False
            sh.com.rep_third_party(f, e)
    
    def load_default(self):
        f = '[MClient] config.Config.load_default'
        if not self.Success:
            sh.com.cancel(f)
            return
        code = sh.ReadTextFile(self.pdefault).get()
        if not code:
            self.Success = False
            sh.com.rep_out(f)
            return
        try:
            self.default = json.loads(code)
        except Exception as e:
            self.Success = False
            sh.com.rep_third_party(f, e)
    
    def set_local(self):
        f = '[MClient] config.Config.set_local'
        if not self.Success:
            sh.com.cancel(f)
            return
        self.plocal = sh.Home(PRODUCT_LOW).add_config(PRODUCT_LOW + '.json')
    
    def create(self):
        f = '[MClient] config.Config.create'
        if not self.Success:
            sh.com.cancel(f)
            return
        if os.path.exists(self.plocal) and os.path.isfile(self.plocal):
            sh.com.rep_lazy(f)
            return
        ''' Since 'local' dictionary is empty for now, this just clones
            'default' to 'new' similar to 'copy.deepcopy'.
        '''
        self.update()
        self.localize()
        self.save()
    
    def set_default(self):
        f = '[MClient] config.Config.set_default'
        if not self.Success:
            sh.com.cancel(f)
            return
        self.pdefault = sh.objs.get_pdir().add('..', 'resources', 'config', 'default.json')
        # Full path is more intuitive in case the file does not exist
        self.pdefault = os.path.abspath(self.pdefault)
        self.Success = sh.File(self.pdefault).Success
    
    def set_schema(self):
        f = '[MClient] config.Config.set_schema'
        if not self.Success:
            sh.com.cancel(f)
            return
        self.pschema = sh.objs.get_pdir().add('..', 'resources', 'config', 'schema.json')
        # Full path is more intuitive in case the file does not exist
        self.pschema = os.path.abspath(self.pschema)
        self.Success = sh.File(self.pschema).Success
    
    def update(self):
        f = '[MClient] config.Config.update'
        if not self.Success:
            sh.com.cancel(f)
            return
        ''' Python 3.9 or newer is required. Combine dictionaries #1 and #2
            to #3 such that #3 has the values of #1, absent in #2, and existing
            values of #1 are updated with the values of #2. #1 and #2 are
            unchanged.
        '''
        self.new = self.default | self.local
    
    def save(self):
        f = '[MClient] config.Config.save'
        if not self.Success:
            sh.com.cancel(f)
            return
        try:
            code = json.dumps(self.new, ensure_ascii=False, indent=4)
        except Exception as e:
            self.Success = False
            sh.com.rep_third_party(f, e)
            return
        self.Success = sh.WriteTextFile(self.plocal, True).write(code)
    
    def localize(self):
        f = '[MClient] config.Config.localize'
        if not self.Success:
            sh.com.cancel(f)
            return
        self.new['columns']['1']['type'] = _(self.new['columns']['1']['type'])
        self.new['columns']['2']['type'] = _(self.new['columns']['2']['type'])
        self.new['columns']['3']['type'] = _(self.new['columns']['3']['type'])
        self.new['columns']['4']['type'] = _(self.new['columns']['4']['type'])
        self.new['subjects']['blocked'] = [_(subj) for subj in self.new['subjects']['blocked']]
        self.new['subjects']['prioritized'] = [_(subj) for subj in self.new['subjects']['prioritized']]
        self.new['lang1'] = _(self.new['lang1'])
        self.new['lang2'] = _(self.new['lang2'])
        self.new['source'] = _(self.new['source'])
        self.new['speech1'] = _(self.new['speech1'])
        self.new['speech2'] = _(self.new['speech2'])
        self.new['speech3'] = _(self.new['speech3'])
        self.new['speech4'] = _(self.new['speech4'])
        self.new['speech5'] = _(self.new['speech5'])
        self.new['speech6'] = _(self.new['speech6'])
        self.new['speech7'] = _(self.new['speech7'])
        self.new['style'] = _(self.new['style'])
    
    def run(self):
        self.set_schema()
        self.load_schema()
        self.set_default()
        self.load_default()
        self.check_default()
        self.set_local()
        self.create()
        self.load_local()
        self.check_local()
        self.update()



class Objects:
    
    def __init__(self):
        self.config = None
    
    def get_config(self):
        if self.config is None:
            self.config = Config()
            self.config.run()
        return self.config


objs = Objects()


if __name__ == '__main__':
    f = '[MClient] config.__main__'
    sh.com.start()
    timer = sh.Timer(f)
    timer.start()
    #objs.get_config().new["PrioritizeSubjects"] = False
    objs.get_config().save()
    timer.end()
    mes = f'Success: {objs.config.Success}'
    sh.objs.get_mes(f, mes).show_info()
    mes = _('Goodbye!')
    sh.objs.get_mes(f, mes, True).show_debug()
    sh.com.end()
