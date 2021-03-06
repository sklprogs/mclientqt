#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from skl_shared.localize import _
import skl_shared.shared as sh

DEBUG = True


class Offline:
    
    def __init__(self):
        self.maxrows = 0
    
    def run_multitrancom(self):
        import plugins.multitrancom.cleanup as cu
        import plugins.multitrancom.tags as tg
        import plugins.multitrancom.elems as el
        file = '/home/pete/bin/mclient/tests/multitrancom (saved in browser)/hello (2021-03-14).html'
        self.htm = sh.ReadTextFile(file).get()
        self.text = cu.CleanUp(self.htm).run()
        itags = tg.Tags (text = self.text
                        ,Debug = DEBUG
                        ,maxrows = self.maxrows
                        )
        blocks = itags.run()
        blocks = el.Elems (blocks = blocks
                          ,Debug = DEBUG
                          ,maxrows = self.maxrows
                          ).run()



class ArticleSubjects:
    
    def __init__(self):
        self.blocks = []
    
    def run(self):
        self.set_blocks()
        self.set_article()
    
    def set_article(self):
        f = '[MClient] tests.Subjects.set_article'
        import subjects.subjects as sj
        import mclient
        pairs = mclient.objs.get_blocksdb().get_dic_pairs()
        mes = _('Pairs: {}').format(pairs)
        sh.objs.get_mes(f,mes,True).show_debug()
        sj.objs.get_article().reset(pairs,DEBUG)
        sj.objs.article.run()
    
    def set_blocks(self):
        f = '[MClient] tests.Subjects.set_blocks'
        import mclient
        # Lists will be automatically read from files on import
        import logic as lg
        #search = 'hello'
        #url = 'https://www.multitran.com/m.exe?s=hello&l1=1&l2=2&SHL=2'
        search = 'messenger'
        url = 'https://www.multitran.com/m.exe?s=messenger&l1=1&l2=2'
        blocks = lg.objs.get_plugins().request (search = search
                                               ,url = url
                                               )
        mclient.objs.get_blocksdb().artid = 1
        data = lg.com.dump_elems (blocks = blocks
                                 ,artid = mclient.objs.blocksdb.artid
                                 )
        if data:
            mclient.objs.blocksdb.fill_blocks(data)
        else:
            sh.com.rep_empty(f)



class Block:
    
    def __init__(self):
        self.id_ = None   # (00) Autoincrement
        self.artid = 0    # (01) ARTICLEID
        self.dic = ''     # (02) DIC (short title)
        self.wform = ''   # (03) WFORM
        self.speech = ''  # (04) SPEECH
        self.transc = ''  # (05) TRANSC
        self.term = ''    # (06) TERM
        self.type_ = ''   # (07) TYPE
        self.text = ''    # (08) TEXT
        self.url = ''     # (09) URL
        self.block = 0    # (10) BLOCK
        self.dprior = 0   # (11) DICPR
        self.select = 0   # (12) SELECTABLE
        self.same = 0     # (13) SAMECELL
        self.cellno = 0   # (14) CELLNO
        self.rowno = -1   # (15) ROWNO
        self.colno = -1   # (16) COLNO
        self.pos1 = -1    # (17) POS1
        self.pos2 = -1    # (18) POS2
        self.node1 = ''   # (19) NODE1
        self.node2 = ''   # (20) NODE2
        self.offpos1 = -1 # (21) OFFPOS1
        self.offpos2 = -1 # (22) OFFPOS2
        self.bbox1 = -1   # (23) BBOX1
        self.bbox2 = -1   # (24) BBOX2
        self.bboy1 = -1   # (25) BBOY1
        self.bboy2 = -1   # (26) BBOY2
        self.textlow = '' # (27) TEXTLOW
        self.ignore = 0   # (28) IGNORE
        self.sprior = 0   # (29) SPEECHPR
        self.dicf = ''    # (30) DIC (full title)
    
    def dump(self):
        return (self.id_
               ,self.artid
               ,self.dic
               ,self.wform
               ,self.speech
               ,self.transc
               ,self.term
               ,self.type_
               ,self.text
               ,self.url
               ,self.block
               ,self.dprior
               ,self.select
               ,self.same
               ,self.cellno
               ,self.rowno
               ,self.colno
               ,self.pos1
               ,self.pos2
               ,self.node1
               ,self.node2
               ,self.offpos1
               ,self.offpos2
               ,self.bbox1
               ,self.bbox2
               ,self.bboy1
               ,self.bboy2
               ,self.textlow
               ,self.ignore
               ,self.speech
               ,self.dicf
               )



class Get:
    
    def run_dsl(self):
        f = '[MClient] tests.Get.run_dsl'
        import plugins.dsl.get as gt
        gt.PATH = sh.Home('mclient').add_config('dics')
        gt.Get (pattern = 'computer'
               ,Debug = DEBUG
               ).run()
    
    def run_multitrancom(self):
        f = '[MClient] tests.Get.run_multitrancom'
        import plugins.multitrancom.get as gt
        #url = 'https://www.multitran.com/m.exe?a=3&sc=8&s=%D1%81%D0%B8%D0%BC%D0%BF%D1%82%D0%BE%D0%BC&l1=2&l2=1&SHL=2'
        #search = '????????????????'
        url = 'https://www.multitran.com/m.exe?s=working%20documentation&l1=1&l2=2&SHL=2'
        search = 'working documentation'
        timer = sh.Timer(f)
        timer.start()
        result = gt.Get (search = search
                        ,url = url
                        ).run()
        timer.end()
        sh.com.run_fast_txt(result)
    
    def run_stardict(self):
        f = '[MClient] tests.Get.run_stardict'
        import logic as lg
        import plugins.stardict.get as sd
        #search = '??????????????????'
        search = 'computer'
        timer = sh.Timer(f)
        timer.start()
        result = sd.Get(search).run()
        timer.end()
        sh.com.run_fast_txt(result)



class Tags:
    
    def run_dsl(self):
        f = '[MClient] tests.Tags.run_dsl'
        import plugins.dsl.get as gt
        import plugins.dsl.cleanup as cu
        import plugins.dsl.tags as tg
        gt.PATH = sh.Home('mclient').add_config('dics')
        articles = gt.Get('account balance').run()
        blocks = []
        for iarticle in articles:
            code = cu.CleanUp(iarticle.code).run()
            code = cu.TagLike(code).run()
            blocks += tg.Tags (code = code
                              ,Debug = DEBUG
                              ,maxrows = 0
                              ,dicname = iarticle.dic
                              ).run()
    
    def analyze_tag(self):
        import plugins.multitrancom.tags as tg
        #tag = '<tr><td class="subj" width="1"><a href="https://www.multitran.com/m.exe?a=110&amp;l1=2&amp;l2=1&amp;s=%D1%82%D1%80%D0%BE%D1%81&amp;sc=371" title="????????????????????">??????????????.'
        #tag = '''<tr><td class="subj" width="1"><a href="https://www.multitran.com/m.exe?a=110&amp;l1=2&amp;l2=1&amp;s=%D1%82%D1%80%D0%BE%D1%81&amp;sc=0" title="?????????? ??????????????">??????.'''
        tag = '<tr><td class="subj" width="1"><a href="https://www.multitran.com/m.exe?a=110&amp;l1=2&amp;l2=1&amp;s=%D1%82%D1%80%D0%BE%D1%81&amp;sc=134" title="??????????????????????">????.'
        itag = tg.AnalyzeTag(tag)
        itag.run()
        itag.debug()
    
    def run_stardict(self):
        f = '[MClient] tests.Tags.run_stardict'
        import plugins.stardict.cleanup as sdcleanup
        import plugins.stardict.tags as sdtags
        file = '/home/pete/bin/mclient/tests/stardict/EnRu full cut.txt'
        text = sh.ReadTextFile(file).get()
        text = sdcleanup.CleanUp(text).run()
        sdtags.Tags (text = text
                    ,Debug = DEBUG
                    ).run()
    
    def run_multitrancom(self):
        f = '[MClient] tests.Tags.run_multitrancom'
        import plugins.multitrancom.cleanup as cu
        import plugins.multitrancom.tags as tg
        ''' #NOTE: The file should be generated with
            'plugins.multitrancom.get.Get', otherwise, 'Tags' will fail
            to set 'dic' and some other types.
        '''
        #file = '/home/pete/bin/mclient/tests/multitrancom (saved in browser)/hello (???????????????????????? ????????) (2021-03-17).html'
        #file = '/home/pete/bin/mclient/tests/multitrancom (saved in browser)/generic drug (2021-03-17).html'
        file = '/home/pete/bin/mclient/tests/multitrancom (saved in browser)/get out of (2021-03-17).html'
        text = sh.ReadTextFile(file).get()
        text = cu.CleanUp(text).run()
        tg.Tags (text = text
                ,Debug = DEBUG
                ,maxrows = 0
                ).run()



class Plugin:
    
    def run_multitrandem(self):
        f = '[MClient] tests.Plugin.run_multitrandem'
        import plugins.multitrandem.get
        import plugins.multitrandem.run as mb
        #search = 'Kafir'
        search = 'abasin'
        #search = 'a posteriori'
        #search = 'abed'
        #search = 'accommodation coefficient'
        #search = 'according'
        #search = '?????????????????? ????????????'
        #search = 'build market'
        #search = 'bunching device'
        #search = 'valve rocker shank'
        # ??????????, ?????????????????????????????? ???????????????????????? ??????????????????
        #search = 'velocity bed'
        #???????????????????? ???????????? ???????????? ?? ???? ?????????????????????? = quininism
        url = ''
        
        ''' #NOTE: This is a standard 'dics' folder, do not include
            subfolders here.
        '''
        plugins.multitrandem.get.PATH = '/home/pete/.config/mclient/dics'
        iplug = mb.Plugin (Debug = DEBUG
                          ,maxrows = 150
                          )
        
        blocks = iplug.request (url = url
                               ,search = search
                               )
        if not blocks:
            blocks = []
        for i in range(len(blocks)):
            mes = '{}: {}: "{}"'.format (i,blocks[i].type_
                                        ,blocks[i].text
                                        )
            print(mes)
    
    def run_stardict(self):
        f = '[MClient] tests.Plugin.run_stardict'
        import plugins.stardict.run as sr
        search = 'about'
        iplug = sr.Plugin(Debug=DEBUG)
        iplug.request(search=search)
    
    def run_dsl(self):
        f = '[MClient] tests.Plugin.run_dsl'
        import plugins.dsl.get
        import plugins.dsl.run as dr
        plugins.dsl.get.DEBUG = DEBUG
        plugins.dsl.get.PATH = sh.Home('mclient').add_config('dics')
        #search = '??????????????????'
        #search = 'computer'
        #search = 'bunker'
        search = 'accounting'
        iplug = dr.Plugin(Debug=DEBUG)
        iplug.request(search=search)
        mes = _('Number of blocks: {}').format(len(iplug.blocks))
        sh.objs.get_mes(f,mes,True).show_debug()
        mes = _('Web-page:') + '\n' + iplug.htm
        sh.com.run_fast_debug(f,mes)
        mes = _('Text:') + '\n' + iplug.text
        sh.com.run_fast_debug(f,mes)
    
    def run_multitrancom(self):
        f = '[MClient] tests.Plugin.run_multitrancom'
        import plugins.multitrancom.run as mc
        #url = 'https://www.multitran.com/m.exe?s=memory%20pressure&l1=2&l2=1&SHL=2'
        #search = 'memory pressure'
        #url = 'https://www.multitran.com/m.exe?s=nucleoside%20reverse%20transcriptase%20inhibitors&l1=2&l2=1&SHL=2'
        #search = 'nucleoside reverse transcriptase inhibitors'
        #url = 'https://www.multitran.com/m.exe?s=%D0%BD%D1%83%D0%BA%D0%BB%D0%B5%D0%B8%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9&l1=2&l2=1&SHL=2'
        #search = '??????????????????????'
        #url = 'https://www.multitran.com/m.exe?a=3&l1=2&l2=1&s=%D0%B2%2B%D1%8F%D0%B1%D0%BB%D0%BE%D1%87%D0%BA%D0%BE&SHL=2'
        #search = '47 ????????'
        #url = 'https://www.multitran.com/m.exe?s=Antiquity&l1=1&l2=2&SHL=2'
        #search = 'Antiquity'
        #url = 'https://www.multitran.com/m.exe?s=hello&l1=1&l2=2&SHL=2'
        #search = 'hello'
        #url = 'https://www.multitran.com/m.exe?s=set&l1=1&l2=2&SHL=2'
        #search = 'set'
        #url = 'https://www.multitran.com/m.exe?a=3&l1=1&l2=2&s=hello&SHL=2'
        #search = '97 ???????? ?? 16 ??????????????????'
        #url = 'https://www.multitran.com/m.exe?a=3&l1=1&l2=2&s=icon&SHL=2'
        #search = 'icon'
        #url = 'https://www.multitran.com/m.exe?a=3&l1=1&l2=2&s=heaven+and+hell+bond&SHL=2'
        #search = 'heaven and hell bond'
        #url = 'https://www.multitran.com/m.exe?s=%D0%B7%D0%B0%D0%B4%D0%B0%D1%87%D0%B0&l1=1&l2=2&SHL=2'
        #search = '????????????'
        #url = 'https://www.multitran.com/m.exe?s=ntthing&l1=1&l2=2&SHL=2'
        #search = 'ntthing'
        #url = 'https://www.multitran.com/m.exe?s=question&l1=2&l2=1&SHL=2'
        #search = 'question'
        #url = 'https://www.multitran.com/m.exe?s=%D1%86%D0%B5%D0%BF%D1%8C:+%D0%BF%D1%80%D0%BE%D0%B2%D0%BE%D0%B4&l1=2&l2=1'
        #search = '????????: ????????????'
        #url = 'https://www.multitran.com/m.exe?s=%D0%B2%D1%81%D0%BF%D0%BE%D0%BC%D0%B8%D0%BD%D0%B0%D1%82%D1%8C&l1=2&l2=1&SHL=2'
        #search = '????????????????????'
        url = 'https://www.multitran.com/m.exe?s=reticulated+siren&l1=1&l2=10000&SHL=33'
        search = 'reticulated siren'
        
        mc.Plugin (Debug = DEBUG
                  ,maxrows = 0
                  ).request (url = url
                            ,search = search
                            )
    
    def reinsert_same(self):
        f = '[MClient] tests.Plugin.reinsert_same'
        import plugins.multitrancom.run as mc
        search = 'set'
        url = 'https://www.multitran.com/m.exe?l1=1&l2=2&s=set'
        timer = sh.Timer('Getting elems')
        timer.start()
        blocks = mc.Plugin().request (url = url
                                     ,search = search
                                     )
        timer.end()
        same = [block for block in blocks if block.same == 1]
        separate = [block for block in blocks if block.same == 0]
        # takes ~1s for 'set' (EN-RU) on AMD E-300
        timer = sh.Timer(f)
        timer.start()
        cells = []
        for block in separate:
            cell = [block]
            for item in same:
                if item.cellno == block.cellno:
                    cell.append(item)
            cells.append(cell)
        timer.end()
        print('Number of blocks:',len(blocks))
        print('Number of cells:',len(cells))



class Commands:
    
    def run_settings(self):
        import config as cf
        import logic as lg
        import settings.controller as st
        cf.DefaultKeys()
        lg.com.load_config()
        st.objs.get_settings().show()
    
    def get_priority(self):
        f = '[MClient] tests.Commands.get_priority'
        import logic as lg
        import subjects.subjects as sj
        title = 'Gruzovik, ??????????????'
        result = sj.objs.get_order().get_priority(title)
        sh.objs.get_mes(f,result,True).show_debug()
    
    def get_column_width(self):
        f = '[MClient] tests.Commands.get_column_width'
        import logic as lg
        #sh.lg.globs['int']['colnum'] = 0
        width = lg.com.get_column_width()
        mes = '"{}%"'.format(width)
        sh.objs.get_mes(f,mes,True).show_debug()
    
    def check_width(self):
        import mclient as mc
        file = '/home/pete/tmp/frame rate.htm'
        #file = '/tmp/f.htm'
        code = sh.ReadTextFile(file).get()
        mc.objs.get_webframe().fill(code)
        mc.objs.webframe.show()
    
    def get_subjects_wo_majors(self):
        ''' Get subjects not united by a major subject. This is not
            an error and can be witnessed sometimes at multitran.com.
        '''
        f = '[MClient] tests.Commands.get_subjects_wo_majors'
        import plugins.multitrancom.subjects as sj
        titles = []
        for key in sj.SUBJECTS.keys():
            if not sj.SUBJECTS[key]['major_en'] \
            and sj.SUBJECTS[key]['Single']:
                titles.append(sj.SUBJECTS[key]['en']['title'])
        titles = sorted(set(titles))
        if titles:
            mes = '\n'.join(titles)
            sh.com.run_fast_debug(f,mes)
        else:
            sh.com.rep_lazy(f)
    
    def get_modified_subjects(self):
        f = '[MClient] tests.Commands.get_modified_subjects'
        import plugins.multitrancom.subjects as sj
        titles = []
        for key in sj.SUBJECTS.keys():
            if sj.SUBJECTS[key]['Modified']:
                titles.append(sj.SUBJECTS[key]['ru']['title'])
        titles.sort()
        mes = '\n'.join(titles)
        sh.com.run_fast_debug(f,mes)
    
    def get_majors_en(self):
        f = '[MClient] tests.Commands.get_majors_en'
        import plugins.multitrancom.subjects as sj
        groups = []
        shorts = []
        titles = []
        for key in sj.SUBJECTS.keys():
            if sj.SUBJECTS[key]['Major']:
                groups.append(sj.SUBJECTS[key]['major_en'])
                shorts.append(sj.SUBJECTS[key]['en']['short'])
                titles.append(sj.SUBJECTS[key]['en']['title'])
        nos = [i + 1 for i in range(len(groups))]
        headers = (_('#'),_('MAJOR (EN)'),_('SHORT'),_('TITLE'))
        iterable = [nos,groups,shorts,titles]
        mes = sh.FastTable (iterable = iterable
                           ,headers = headers
                           ,maxrow = 30
                           ).run()
        sh.com.run_fast_debug(f,mes)
    
    def get_majors(self):
        import plugins.multitrancom.subjects as sj
        print(sj.objs.get_subjects().get_majors())
    
    def run_speech(self):
        import logic as lg
        order = (_('Noun'),_('Verb'),_('Adjective'))
        lg.objs.get_speech_prior().reset(order)
        lg.objs.speech_prior.debug()
    
    def generate_config(self):
        import config as cf
        cf.CreateConfig().run()
    
    def edit_priorities(self):
        import mclient as mc
        import logic as lg
        mc.objs.get_priorities().reset (lst1 = lg.objs.get_order().priorlst
                                       ,lst2 = lg.objs.get_plugins().get_subjects()
                                       ,art_subjects = []
                                       ,majors = lg.objs.plugins.get_majors()
                                       )
        mc.objs.priorities.show()
    
    def edit_blacklist(self):
        import mclient as mc
        import logic as lg
        mc.objs.get_blacklist().reset (lst1 = lg.objs.get_order().blacklst
                                      ,lst2 = lg.objs.get_plugins().get_subjects()
                                      ,art_subjects = []
                                      ,majors = lg.objs.plugins.get_majors()
                                      )
        mc.objs.blacklist.show()
    
    def show_about(self):
        from mclient import About
        About().show()
    
    def get_nonpairs(self):
        ''' Get languages that are not supported by multitran.com for
            both directions.
        '''
        f = '[MClient] tests.Commands.get_nonpairs'
        import plugins.multitrancom.pairs as pairs
        lst = []
        for lang in pairs.LANGS:
            pairs1 = pairs.objs.get_pairs().get_pairs1(lang)
            pairs2 = pairs.objs.get_pairs().get_pairs2(lang)
            if not pairs1:
                pairs1 = []
            if not pairs2:
                pairs2 = []
            if pairs1 != pairs2:
                for xlang in pairs1:
                    if xlang not in pairs2:
                        lst.append('{}-{}'.format(xlang,lang))
                for xlang in pairs2:
                    if xlang not in pairs1:
                        lst.append('{}-{}'.format(lang,xlang))
        lst = list(set(lst))
        lst.sort()
        mes = _('The following pairs are not supported:\n{}')
        mes = mes.format(lst)
        sh.objs.get_mes(f,mes,True).show_info()
    
    def compare_elems(self):
        f = '[MClient] tests.Commands.compare_elems'
        import plugins.multitran.elems as el
        data1 = []
        data2 = []
        # Create blocks
        #1 #1
        block = list(Block().dump())
        block[2] = '?????????? ??????????????' # DIC
        block[30] = '??????.'         # DICF
        block[7] = 'term'          # TYPE
        block[8] = 'hello'         # TEXT
        data1.append(block)
        #1 #2
        block = list(Block().dump())
        block[2] = '?????????? ??????????????' # DIC
        block[30] = '??????.'         # DICF
        block[7] = 'comment'       # TYPE
        block[8] = 'yes'           # TEXT
        data1.append(block)
        #1 #3
        block = list(Block().dump())
        block[2] = '?????????? ??????????????' # DIC
        block[30] = '??????.'         # DICF
        block[7] = 'term'          # TYPE
        block[8] = 'goodbye'       # TEXT
        data1.append(block)
        #2 #1
        block = list(Block().dump())
        block[2] = '?????????? ??????????????' # DIC
        block[30] = '??????.'         # DICF
        block[7] = 'term'          # TYPE
        block[8] = 'goodbye'       # TEXT
        data2.append(block)
        #2 #2
        block = list(Block().dump())
        block[2] = '????????????????????'    # DIC
        block[30] = '????????????.'      # DICF
        block[7] = 'comment'       # TYPE
        block[8] = 'yes'           # TEXT
        data2.append(block)
        #2 #3
        block = list(Block().dump())
        block[2] = '?????????? ??????????????' # DIC
        block[30] = '??????.'         # DICF
        block[7] = 'term'          # TYPE
        block[8] = 'hello'         # TEXT
        data2.append(block)
        # Compare
        data = el.Elems(data1,data2).run()
        data = [str(item) for item in data]
        data = '\n'.join(data)
        sh.com.run_fast_txt(data)
    
    def request(self):
        f = '[MClient] tests.Commands.request'
        source = _('Multitran')
        pair = 'DEU <=> RUS'
        search = 'ern??hrung'
        mes = 'Source: "{}"; pair: "{}"; search: "{}"'.format (source
                                                              ,pair
                                                              ,search
                                                              )
        lg.objs.get_plugins().set(source)
        lg.objs.plugins.set_pair(pair)
        sh.objs.get_mes(f,mes,True).show_info()
        data = lg.objs.plugins.request (search = search
                                       ,url = ''
                                       )
        if data:
            sh.com.run_fast_txt(data)
        else:
            sh.com.rep_empty(f)
    
    def get_url(self):
        f = '[MClient] tests.Commands.get_url'
        source = 'multitran.com'
        pair = 'RUS <=> XAL'
        search = '???? ????????????????!'
        mes = 'Source: "{}"; pair: "{}"; search: "{}"'
        mes = mes.format(source,pair,search)
        lg.objs.get_plugins().set(source)
        lg.objs.plugins.set_pair(pair)
        sh.objs.get_mes(f,mes,True).show_info()
        lg.objs.plugins.get_url(search)
    
    def suggest(self):
        f = '[MClient] tests.Commands.suggest'
        source = 'multitran.com'
        pair = 'DEU <=> RUS'
        search = 'Schei??e'
        mes = 'Source: "{}"; pair: "{}"; search: "{}"'
        mes = mes.format(source,pair,search)
        lg.objs.get_plugins().set(source)
        lg.objs.plugins.set_pair(pair)
        sh.objs.get_mes(f,mes,True).show_info()
        lg.com.suggest(search)
    
    def _set_timeout(self,module,source,timeout):
        f = '[MClient] tests.Commands._set_timeout'
        lg.objs.get_plugins().set(source)
        lg.objs.plugins.set_timeout(timeout)
        mes = 'Source: {}; Timeout: {}'.format (source
                                               ,module.TIMEOUT
                                               )
        sh.objs.get_mes(f,mes,True).show_debug()
    
    def set_timeout(self):
        f = '[MClient] tests.Commands.set_timeout'
        import plugins.multitrancom.get as mc
        import plugins.stardict.get as sd
        self._set_timeout (module = sd
                          ,source = _('Offline')
                          ,timeout = 1
                          )
        self._set_timeout (module = mc
                          ,source = _('Multitran')
                          ,timeout = 2
                          )
        self._set_timeout (module = mc
                          ,source = 'multitran.com'
                          ,timeout = 3
                          )
    
    def is_accessible(self):
        f = '[MClient] tests.Commands.is_accessible'
        source = _('Offline')
        lg.objs.get_plugins().set(source)
        result = lg.objs.plugins.is_accessible()
        mes = 'Source: {}; Accessibility: {}'.format(source,result)
        sh.objs.get_mes(f,mes,True).show_debug()
        source = 'multitran.com'
        lg.objs.plugins.set(source)
        result = lg.objs.plugins.is_accessible()
        mes = 'Source: {}; Accessibility: {}'.format(source,result)
        sh.objs.get_mes(f,mes,True).show_debug()
    
    def welcome(self):
        f = '[MClient] tests.Commands.welcome'
        file_w = '/tmp/test.html'
        code = lg.Welcome().run()
        if code:
            sh.WriteTextFile(file_w).write(code)
            sh.Launch(file_w).default()
        else:
            sh.com.rep_empty(f)
    
    def set_pair(self):
        f = '[MClient] tests.Commands.set_pair'
        import plugins.multitrancom.get
        pair = 'RUS <=> XAL'
        source = 'multitran.com'
        lg.objs.get_plugins().set(source)
        lg.objs.plugins.set_pair(pair)
        
        mes = '{}: {}'.format(source,plugins.multitrancom.get.PAIR)
        sh.objs.get_mes(f,mes,True).show_debug()
        pair = 'XAL <=> RUS'
        source = _('Multitran')
        lg.objs.plugins.set(source)
        lg.objs.plugins.set_pair(pair)
        mes = 'multitrancom: {}'.format(plugins.multitrancom.get.PAIR)
        sh.objs.get_mes(f,mes,True).show_debug()
        
    def translate_gui (self,source,pair
                      ,search,url
                      ):
        f = '[MClient] tests.Commands.translate_gui'
        import mclient
        lg.objs.get_plugins().set(source)
        lg.objs.plugins.set_pair(pair)
        lg.objs.get_request().search = search
        lg.objs.request.url = url
        mclient.objs.webframe().load_article()
        mclient.objs.webframe.gui.show()
    
    def translate_cli (self,source,pair
                      ,search,url,maxrows=100
                      ):
        f = '[MClient] tests.Commands.translate_cli'
        import cells as cl
        lg.objs.get_plugins().set(source)
        lg.objs.plugins.set_pair(pair)
        lg.objs.get_request().search = search
        lg.objs.request.url = url
        data = lg.objs.plugins.request (search = search
                                       ,url = url
                                       )
        cldata = []
        for i in range(len(data)):
            row = [i,data[i][7],data[i][8],data[i][13],data[i][2]
                  ,data[i][3],data[i][4],data[i][5]
                  ]
            cldata.append(row)
        cells = cl.Cells (data = cldata
                         ,cols = ('dic','wform','transc','speech')
                         ,collimit = 8
                         ,phdic = ''
                         ,Reverse = False
                         ,ExpandSp = False
                         ,Debug = DEBUG
                         ,maxrows = maxrows
                         )
        cells.run()
    
    def translate (self,source,pair
                  ,search,url,maxrows=100
                  ,GUI=False
                  ):
        if GUI:
            self.translate_gui (source = source
                               ,pair = pair
                               ,search = search
                               ,url = url
                               )
        else:
            self.translate_cli (source = source
                               ,pair = pair
                               ,search = search
                               ,url = url
                               ,maxrows = maxrows
                               )
            
    
    def run_com_complex(self,GUI=False):
        self.translate (source = 'multitran.com'
                       ,pair = 'ENG <=> RUS'
                       ,search = 'complex'
                       ,url = 'https://www.multitran.com/m.exe?s=complex&l1=2&l2=1&SHL=2'
                       ,GUI = GUI
                       )
    
    def run_com_abatis2(self,GUI=False):
        self.translate (source = 'multitran.com'
                       ,pair = 'ENG <=> RUS'
                       ,search = 'abatis'
                       ,url = 'https://www.multitran.com/m.exe?s=abatis&l1=2&l2=1&SHL=2'
                       ,GUI = GUI
                       )
    
    def run_com_abatis(self,GUI=False):
        self.translate (source = 'multitran.com'
                       ,pair = 'ENG <=> RUS'
                       ,search = '????????????'
                       ,url = 'https://www.multitran.com/m.exe?s=%D0%B7%D0%B0%D1%81%D0%B5%D0%BA%D0%B0&l1=2&l2=1&SHL=2'
                       ,GUI = GUI
                       )
    
    def run_all_ernahrung(self,GUI=False):
        self.translate (source = _('Multitran')
                       ,pair = 'DEU <=> RUS'
                       ,search = 'ern??hrung'
                       ,url = 'https://www.multitran.com/m.exe?s=ern%C3%A4hrung&l1=3&l2=2&SHL=2'
                       ,GUI = GUI
                       )
    
    def run_com_mud(self,GUI=False):
        self.translate (source = 'multitran.com'
                       ,pair = 'ENG <=> RUS'
                       ,search = 'mud'
                       ,url = 'https://multitran.com/m.exe?s=mud&l1=1&l2=2&SHL=2'
                       ,GUI = GUI
                       )
    
    def run_com_systemwide(self,GUI=False):
        self.translate (source = 'multitran.com'
                       ,pair = 'ENG <=> RUS'
                       ,search = 'system-wide'
                       ,url = 'https://www.multitran.com/m.exe?s=system-wide&l1=2&l2=1&SHL=2'
                       ,GUI = GUI
                       )
    
    def go_keyboard(self,event=None):
        f = '[MClient] tests.Commands.go_keyboard'
        mes = _('Triggered!')
        sh.objs.get_mes(f,mes,True).show_debug()
    
    def copy_text(self,event=None):
        f = '[MClient] tests.Commands.copy_text'
        mes = _('Triggered!')
        sh.objs.get_mes(f,mes,True).show_debug()



class DB:
    
    def __init__(self,Debug=False):
        # 'mandatory -> ?????????????????????? ????????'
        lg.objs.get_request().search = '?????????????????????? ????????'
        lg.objs.request.url = 'https://www.multitran.com/m.exe?a=3&sc=716&s=mandatory&l1=1&l2=2&SHL=2'
        self.maxrows = 1000
        lg.objs.get_plugins (Debug = Debug
                            ,maxrows = self.maxrows
                            )
    
    def get(self):
        f = '[MClient] tests.DB.get'
        result = lg.objs.get_blocksdb().get_max_col_no()
        sh.objs.get_mes(f,result,True).show_debug()
        lg.objs.blocksdb.print_custom()
    
    def run(self):
        self.fill()
        self.get()
    
    def fill(self):
        f = '[MClient] tests.DB.fill'
        blocks = lg.objs.get_plugins().request (search = lg.objs.get_request().search
                                               ,url = lg.objs.request.url
                                               )
        # 'None' skips the autoincrement
        data = (None                              # (00) ARTICLEID
               ,sh.lg.globs['str']['source']      # (01) SOURCE
               ,lg.objs.request.search            # (02) TITLE
               ,lg.objs.request.url               # (03) URL
               ,lg.objs.get_plugins().get_lang1() # (04) LANG1
               ,lg.objs.plugins.get_lang2()       # (05) LANG2
               ,None                              # (06) BOOKMARK
               ,lg.objs.plugins.get_htm()         # (07) CODE
               )
        lg.objs.get_blocksdb().fill_articles(data)
        lg.objs.blocksdb.artid = lg.objs.blocksdb.get_max_artid()
        data = lg.com.dump_elems (blocks = blocks
                                 ,artid = lg.objs.blocksdb.artid
                                 )
        if data:
            lg.objs.blocksdb.fill_blocks(data)
            
        lg.objs.blocksdb.update_phterm()
        
        self.phdic = lg.objs.blocksdb.get_phdic()
        if self.phdic:
            if sh.lg.globs['bool']['ShortSubjects']:
                self.phdic = self.phdic[0]
            else:
                self.phdic = self.phdic[1]
        else:
            self.phdic = ''
        
        if self.phdic:
            lg.objs.request.SpecialPage = False
        else:
            # Otherwise, 'SpecialPage' will be inherited
            lg.objs.request.SpecialPage = True
        #self.update_columns()
        
        SortTerms = sh.lg.globs['bool']['AlphabetizeTerms'] \
                    and not lg.objs.request.SpecialPage
        ''' We must reset DB as early as possible after setting 'elems',
            otherwise, real and loaded settings may not coincide, which,
            in turn, may lead to a data loss, see, for example, RU-EN:
            "????????: ????????????".
        '''
        lg.objs.blocksdb.reset (cols = lg.objs.request.cols
                               ,SortRows = sh.lg.globs['bool']['SortByColumns']
                               ,SortTerms = SortTerms
                               ,ExpandDic = not sh.lg.globs['bool']['ShortSubjects']
                               ,ShowUsers = sh.lg.globs['bool']['ShowUserNames']
                               ,PhraseCount = sh.lg.globs['bool']['PhraseCount']
                               )
        sj.objs.get_article().reset (pairs = lg.objs.blocksdb.get_dic_pairs()
                                    ,Debug = lg.objs.get_plugins().Debug
                                    )
        sj.objs.article.run()
        data = lg.objs.blocksdb.assign_bp()
        spdic = lg.objs.get_speech_prior().get_all2prior()
        bp = cl.BlockPrioritize (data = data
                                ,Block = sh.lg.globs['bool']['BlockSubjects']
                                ,Prioritize = sh.lg.globs['bool']['PrioritizeSubjects']
                                ,phdic = self.phdic
                                ,spdic = spdic
                                ,Debug = lg.objs.plugins.Debug
                                ,maxrows = lg.objs.plugins.maxrows
                                )
        bp.run()
        lg.objs.blocksdb.update(bp.query)
        
        lg.objs.blocksdb.unignore()
        lg.objs.blocksdb.ignore()
        
        data = lg.objs.blocksdb.assign_cells()

        if sh.lg.globs['bool']['ShortSpeech']:
            spdic = {}
        else:
            spdic = lg.objs.speech_prior.get_abbr2full()
        
        cells = cl.Cells (data = data
                         ,cols = lg.objs.request.cols
                         ,collimit = lg.objs.request.collimit
                         ,phdic = self.phdic
                         ,spdic = spdic
                         ,Reverse = sh.lg.globs['bool']['VerticalView']
                         ,Debug = lg.objs.plugins.Debug
                         ,maxrows = lg.objs.plugins.maxrows
                         )
        cells.run()
        cells.dump(lg.objs.blocksdb)


com = Commands()


if __name__ == '__main__':
    f = '[MClient] tests.__main__'
    sh.com.start()
    #ArticleSubjects().run()
    #com.check_width()
    #com.edit_blacklist()
    #com.edit_priorities()
    #com.get_column_width()
    #com.get_majors_en()
    #com.get_modified_subjects()
    #com.get_priority()
    #com.get_subjects_wo_majors()
    com.run_settings()
    #com.run_sources()
    #com.show_about()
    #Get().run_dsl()
    #Get().run_multitrancom()
    #Offline().run_multitrancom()
    #Plugin().reinsert_same()
    #Plugin().run_dsl()
    #Plugin().run_multitrandem()
    #Plugin().run_multitrancom()
    #Tags().analyze_tag()
    #Tags().run_dsl()
    #Tags().run_multitrancom()
    #Tags().run_stardict()
    '''
    import logic as lg
    import subjects.subjects as sj
    import cells as cl
    DB(0).run()
    '''
    sh.com.end()
