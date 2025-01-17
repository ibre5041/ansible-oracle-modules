# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 OracleNetServicesV3.g 2021-09-20 11:12:38

import sys
from .antlr3 import *
from .antlr3.compat import set, frozenset

from .antlr3.tree import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
COMMA=11
WORD=6
EQUALS=7
DOUBLE_QUOTE=13
NEWLINE=16
RIGHT_PAREN=9
KEYWORD=5
LEFT_PAREN=8
SINGLE_QUOTE=12
COMMENT=14
ORAFILE=4
WHITESPACE=15
EOF=-1
QUOTED_STRING=10

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "ORAFILE", "KEYWORD", "WORD", "EQUALS", "LEFT_PAREN", "RIGHT_PAREN", 
    "QUOTED_STRING", "COMMA", "SINGLE_QUOTE", "DOUBLE_QUOTE", "COMMENT", 
    "WHITESPACE", "NEWLINE"
]




class OracleNetServicesV3Parser(Parser):
    grammarFileName = "OracleNetServicesV3.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(OracleNetServicesV3Parser, self).__init__(input, state, *args, **kwargs)






        self._adaptor = None
        self.adaptor = CommonTreeAdaptor()
                


        
    def getTreeAdaptor(self):
        return self._adaptor

    def setTreeAdaptor(self, adaptor):
        self._adaptor = adaptor

    adaptor = property(getTreeAdaptor, setTreeAdaptor)

                      
    #@Override
    def reportError(self, e):
        super(OracleNetServicesV3Parser, self).reportError(e)
        raise ValueError('Parser error: {}, {}'.format(e, e.token))


    class configuration_file_return(ParserRuleReturnScope):
        def __init__(self):
            super(OracleNetServicesV3Parser.configuration_file_return, self).__init__()

            self.tree = None




    # $ANTLR start "configuration_file"
    # OracleNetServicesV3.g:64:1: configuration_file : ( parameter )* EOF -> ^( ORAFILE ( parameter )* ) ;
    def configuration_file(self, ):

        retval = self.configuration_file_return()
        retval.start = self.input.LT(1)

        root_0 = None

        EOF2 = None
        parameter1 = None


        EOF2_tree = None
        stream_EOF = RewriteRuleTokenStream(self._adaptor, "token EOF")
        stream_parameter = RewriteRuleSubtreeStream(self._adaptor, "rule parameter")
        try:
            try:
                # OracleNetServicesV3.g:65:5: ( ( parameter )* EOF -> ^( ORAFILE ( parameter )* ) )
                # OracleNetServicesV3.g:65:7: ( parameter )* EOF
                pass 
                # OracleNetServicesV3.g:65:7: ( parameter )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if (LA1_0 == WORD) :
                        alt1 = 1


                    if alt1 == 1:
                        # OracleNetServicesV3.g:65:9: parameter
                        pass 
                        self._state.following.append(self.FOLLOW_parameter_in_configuration_file98)
                        parameter1 = self.parameter()

                        self._state.following.pop()
                        stream_parameter.add(parameter1.tree)


                    else:
                        break #loop1
                EOF2=self.match(self.input, EOF, self.FOLLOW_EOF_in_configuration_file107) 
                stream_EOF.add(EOF2)

                # AST Rewrite
                # elements: parameter
                # token labels: 
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 67:5: -> ^( ORAFILE ( parameter )* )
                # OracleNetServicesV3.g:67:8: ^( ORAFILE ( parameter )* )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.createFromType(ORAFILE, "ORAFILE"), root_1)

                # OracleNetServicesV3.g:67:18: ( parameter )*
                while stream_parameter.hasNext():
                    self._adaptor.addChild(root_1, stream_parameter.nextTree())


                stream_parameter.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "configuration_file"

    class parameter_return(ParserRuleReturnScope):
        def __init__(self):
            super(OracleNetServicesV3Parser.parameter_return, self).__init__()

            self.tree = None




    # $ANTLR start "parameter"
    # OracleNetServicesV3.g:70:1: parameter : k= WORD EQUALS ( value | LEFT_PAREN value_list RIGHT_PAREN | parameter_list ) -> ^( KEYWORD[$k] $k ( value )? ( LEFT_PAREN )? ( value_list )? ( RIGHT_PAREN )? ( parameter_list )? ) ;
    def parameter(self, ):

        retval = self.parameter_return()
        retval.start = self.input.LT(1)

        root_0 = None

        k = None
        EQUALS3 = None
        LEFT_PAREN5 = None
        RIGHT_PAREN7 = None
        value4 = None

        value_list6 = None

        parameter_list8 = None


        k_tree = None
        EQUALS3_tree = None
        LEFT_PAREN5_tree = None
        RIGHT_PAREN7_tree = None
        stream_WORD = RewriteRuleTokenStream(self._adaptor, "token WORD")
        stream_EQUALS = RewriteRuleTokenStream(self._adaptor, "token EQUALS")
        stream_RIGHT_PAREN = RewriteRuleTokenStream(self._adaptor, "token RIGHT_PAREN")
        stream_LEFT_PAREN = RewriteRuleTokenStream(self._adaptor, "token LEFT_PAREN")
        stream_value_list = RewriteRuleSubtreeStream(self._adaptor, "rule value_list")
        stream_value = RewriteRuleSubtreeStream(self._adaptor, "rule value")
        stream_parameter_list = RewriteRuleSubtreeStream(self._adaptor, "rule parameter_list")
        try:
            try:
                # OracleNetServicesV3.g:71:5: (k= WORD EQUALS ( value | LEFT_PAREN value_list RIGHT_PAREN | parameter_list ) -> ^( KEYWORD[$k] $k ( value )? ( LEFT_PAREN )? ( value_list )? ( RIGHT_PAREN )? ( parameter_list )? ) )
                # OracleNetServicesV3.g:71:7: k= WORD EQUALS ( value | LEFT_PAREN value_list RIGHT_PAREN | parameter_list )
                pass 
                k=self.match(self.input, WORD, self.FOLLOW_WORD_in_parameter139) 
                stream_WORD.add(k)
                EQUALS3=self.match(self.input, EQUALS, self.FOLLOW_EQUALS_in_parameter141) 
                stream_EQUALS.add(EQUALS3)
                # OracleNetServicesV3.g:71:21: ( value | LEFT_PAREN value_list RIGHT_PAREN | parameter_list )
                alt2 = 3
                LA2_0 = self.input.LA(1)

                if (LA2_0 == WORD or LA2_0 == QUOTED_STRING) :
                    alt2 = 1
                elif (LA2_0 == LEFT_PAREN) :
                    LA2_2 = self.input.LA(2)

                    if (LA2_2 == WORD) :
                        LA2_3 = self.input.LA(3)

                        if (LA2_3 == EQUALS) :
                            alt2 = 3
                        elif (LA2_3 == RIGHT_PAREN or LA2_3 == COMMA) :
                            alt2 = 2
                        else:
                            nvae = NoViableAltException("", 2, 3, self.input)

                            raise nvae

                    elif (LA2_2 == QUOTED_STRING) :
                        alt2 = 2
                    else:
                        nvae = NoViableAltException("", 2, 2, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # OracleNetServicesV3.g:71:23: value
                    pass 
                    self._state.following.append(self.FOLLOW_value_in_parameter145)
                    value4 = self.value()

                    self._state.following.pop()
                    stream_value.add(value4.tree)


                elif alt2 == 2:
                    # OracleNetServicesV3.g:72:24: LEFT_PAREN value_list RIGHT_PAREN
                    pass 
                    LEFT_PAREN5=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_parameter170) 
                    stream_LEFT_PAREN.add(LEFT_PAREN5)
                    self._state.following.append(self.FOLLOW_value_list_in_parameter172)
                    value_list6 = self.value_list()

                    self._state.following.pop()
                    stream_value_list.add(value_list6.tree)
                    RIGHT_PAREN7=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_parameter174) 
                    stream_RIGHT_PAREN.add(RIGHT_PAREN7)


                elif alt2 == 3:
                    # OracleNetServicesV3.g:73:24: parameter_list
                    pass 
                    self._state.following.append(self.FOLLOW_parameter_list_in_parameter199)
                    parameter_list8 = self.parameter_list()

                    self._state.following.pop()
                    stream_parameter_list.add(parameter_list8.tree)




                # AST Rewrite
                # elements: value, k, LEFT_PAREN, value_list, RIGHT_PAREN, parameter_list
                # token labels: k
                # rule labels: retval
                # token list labels: 
                # rule list labels: 
                # wildcard labels: 

                retval.tree = root_0
                stream_k = RewriteRuleTokenStream(self._adaptor, "token k", k)

                if retval is not None:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "rule retval", retval.tree)
                else:
                    stream_retval = RewriteRuleSubtreeStream(self._adaptor, "token retval", None)


                root_0 = self._adaptor.nil()
                # 75:2: -> ^( KEYWORD[$k] $k ( value )? ( LEFT_PAREN )? ( value_list )? ( RIGHT_PAREN )? ( parameter_list )? )
                # OracleNetServicesV3.g:75:5: ^( KEYWORD[$k] $k ( value )? ( LEFT_PAREN )? ( value_list )? ( RIGHT_PAREN )? ( parameter_list )? )
                root_1 = self._adaptor.nil()
                root_1 = self._adaptor.becomeRoot(self._adaptor.create(KEYWORD, k), root_1)

                self._adaptor.addChild(root_1, stream_k.nextNode())
                # OracleNetServicesV3.g:75:22: ( value )?
                if stream_value.hasNext():
                    self._adaptor.addChild(root_1, stream_value.nextTree())


                stream_value.reset();
                # OracleNetServicesV3.g:75:29: ( LEFT_PAREN )?
                if stream_LEFT_PAREN.hasNext():
                    self._adaptor.addChild(root_1, stream_LEFT_PAREN.nextNode())


                stream_LEFT_PAREN.reset();
                # OracleNetServicesV3.g:75:41: ( value_list )?
                if stream_value_list.hasNext():
                    self._adaptor.addChild(root_1, stream_value_list.nextTree())


                stream_value_list.reset();
                # OracleNetServicesV3.g:75:53: ( RIGHT_PAREN )?
                if stream_RIGHT_PAREN.hasNext():
                    self._adaptor.addChild(root_1, stream_RIGHT_PAREN.nextNode())


                stream_RIGHT_PAREN.reset();
                # OracleNetServicesV3.g:75:66: ( parameter_list )?
                if stream_parameter_list.hasNext():
                    self._adaptor.addChild(root_1, stream_parameter_list.nextTree())


                stream_parameter_list.reset();

                self._adaptor.addChild(root_0, root_1)



                retval.tree = root_0



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "parameter"

    class parameter_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(OracleNetServicesV3Parser.parameter_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "parameter_list"
    # OracleNetServicesV3.g:78:1: parameter_list : ( LEFT_PAREN parameter RIGHT_PAREN )+ ;
    def parameter_list(self, ):

        retval = self.parameter_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        LEFT_PAREN9 = None
        RIGHT_PAREN11 = None
        parameter10 = None


        LEFT_PAREN9_tree = None
        RIGHT_PAREN11_tree = None

        try:
            try:
                # OracleNetServicesV3.g:79:2: ( ( LEFT_PAREN parameter RIGHT_PAREN )+ )
                # OracleNetServicesV3.g:79:4: ( LEFT_PAREN parameter RIGHT_PAREN )+
                pass 
                root_0 = self._adaptor.nil()

                # OracleNetServicesV3.g:79:4: ( LEFT_PAREN parameter RIGHT_PAREN )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == LEFT_PAREN) :
                        alt3 = 1


                    if alt3 == 1:
                        # OracleNetServicesV3.g:79:5: LEFT_PAREN parameter RIGHT_PAREN
                        pass 
                        LEFT_PAREN9=self.match(self.input, LEFT_PAREN, self.FOLLOW_LEFT_PAREN_in_parameter_list285)

                        LEFT_PAREN9_tree = self._adaptor.createWithPayload(LEFT_PAREN9)
                        self._adaptor.addChild(root_0, LEFT_PAREN9_tree)

                        self._state.following.append(self.FOLLOW_parameter_in_parameter_list287)
                        parameter10 = self.parameter()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, parameter10.tree)
                        RIGHT_PAREN11=self.match(self.input, RIGHT_PAREN, self.FOLLOW_RIGHT_PAREN_in_parameter_list289)

                        RIGHT_PAREN11_tree = self._adaptor.createWithPayload(RIGHT_PAREN11)
                        self._adaptor.addChild(root_0, RIGHT_PAREN11_tree)



                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "parameter_list"

    class keyword_return(ParserRuleReturnScope):
        def __init__(self):
            super(OracleNetServicesV3Parser.keyword_return, self).__init__()

            self.tree = None




    # $ANTLR start "keyword"
    # OracleNetServicesV3.g:82:1: keyword : WORD ;
    def keyword(self, ):

        retval = self.keyword_return()
        retval.start = self.input.LT(1)

        root_0 = None

        WORD12 = None

        WORD12_tree = None

        try:
            try:
                # OracleNetServicesV3.g:83:5: ( WORD )
                # OracleNetServicesV3.g:83:7: WORD
                pass 
                root_0 = self._adaptor.nil()

                WORD12=self.match(self.input, WORD, self.FOLLOW_WORD_in_keyword305)

                WORD12_tree = self._adaptor.createWithPayload(WORD12)
                self._adaptor.addChild(root_0, WORD12_tree)




                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "keyword"

    class value_return(ParserRuleReturnScope):
        def __init__(self):
            super(OracleNetServicesV3Parser.value_return, self).__init__()

            self.tree = None




    # $ANTLR start "value"
    # OracleNetServicesV3.g:86:1: value : ( WORD | QUOTED_STRING );
    def value(self, ):

        retval = self.value_return()
        retval.start = self.input.LT(1)

        root_0 = None

        set13 = None

        set13_tree = None

        try:
            try:
                # OracleNetServicesV3.g:87:5: ( WORD | QUOTED_STRING )
                # OracleNetServicesV3.g:
                pass 
                root_0 = self._adaptor.nil()

                set13 = self.input.LT(1)
                if self.input.LA(1) == WORD or self.input.LA(1) == QUOTED_STRING:
                    self.input.consume()
                    self._adaptor.addChild(root_0, self._adaptor.createWithPayload(set13))
                    self._state.errorRecovery = False

                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "value"

    class value_list_return(ParserRuleReturnScope):
        def __init__(self):
            super(OracleNetServicesV3Parser.value_list_return, self).__init__()

            self.tree = None




    # $ANTLR start "value_list"
    # OracleNetServicesV3.g:91:1: value_list : value ( COMMA value )* ;
    def value_list(self, ):

        retval = self.value_list_return()
        retval.start = self.input.LT(1)

        root_0 = None

        COMMA15 = None
        value14 = None

        value16 = None


        COMMA15_tree = None

        try:
            try:
                # OracleNetServicesV3.g:92:5: ( value ( COMMA value )* )
                # OracleNetServicesV3.g:92:7: value ( COMMA value )*
                pass 
                root_0 = self._adaptor.nil()

                self._state.following.append(self.FOLLOW_value_in_value_list347)
                value14 = self.value()

                self._state.following.pop()
                self._adaptor.addChild(root_0, value14.tree)
                # OracleNetServicesV3.g:92:13: ( COMMA value )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == COMMA) :
                        alt4 = 1


                    if alt4 == 1:
                        # OracleNetServicesV3.g:92:15: COMMA value
                        pass 
                        COMMA15=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_value_list351)

                        COMMA15_tree = self._adaptor.createWithPayload(COMMA15)
                        self._adaptor.addChild(root_0, COMMA15_tree)

                        self._state.following.append(self.FOLLOW_value_in_value_list353)
                        value16 = self.value()

                        self._state.following.pop()
                        self._adaptor.addChild(root_0, value16.tree)


                    else:
                        break #loop4



                retval.stop = self.input.LT(-1)


                retval.tree = self._adaptor.rulePostProcessing(root_0)
                self._adaptor.setTokenBoundaries(retval.tree, retval.start, retval.stop)


            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)
                retval.tree = self._adaptor.errorNode(self.input, retval.start, self.input.LT(-1), re)
        finally:

            pass
        return retval

    # $ANTLR end "value_list"


    # Delegated rules


 

    FOLLOW_parameter_in_configuration_file98 = frozenset([6])
    FOLLOW_EOF_in_configuration_file107 = frozenset([1])
    FOLLOW_WORD_in_parameter139 = frozenset([7])
    FOLLOW_EQUALS_in_parameter141 = frozenset([6, 8, 10])
    FOLLOW_value_in_parameter145 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_parameter170 = frozenset([6, 10])
    FOLLOW_value_list_in_parameter172 = frozenset([9])
    FOLLOW_RIGHT_PAREN_in_parameter174 = frozenset([1])
    FOLLOW_parameter_list_in_parameter199 = frozenset([1])
    FOLLOW_LEFT_PAREN_in_parameter_list285 = frozenset([6])
    FOLLOW_parameter_in_parameter_list287 = frozenset([9])
    FOLLOW_RIGHT_PAREN_in_parameter_list289 = frozenset([1, 8])
    FOLLOW_WORD_in_keyword305 = frozenset([1])
    FOLLOW_set_in_value0 = frozenset([1])
    FOLLOW_value_in_value_list347 = frozenset([1, 11])
    FOLLOW_COMMA_in_value_list351 = frozenset([6, 10])
    FOLLOW_value_in_value_list353 = frozenset([1, 11])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from .antlr3.main import ParserMain
    main = ParserMain("OracleNetServicesV3Lexer", OracleNetServicesV3Parser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
