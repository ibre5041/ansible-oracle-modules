# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 OracleNetServicesV3.g 2021-09-20 11:12:38

import sys
from .antlr3 import *
from .antlr3.compat import set, frozenset


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


class OracleNetServicesV3Lexer(Lexer):

    grammarFileName = "OracleNetServicesV3.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(OracleNetServicesV3Lexer, self).__init__(input, state)


        self.dfa4 = self.DFA4(
            self, 4,
            eot = self.DFA4_eot,
            eof = self.DFA4_eof,
            min = self.DFA4_min,
            max = self.DFA4_max,
            accept = self.DFA4_accept,
            special = self.DFA4_special,
            transition = self.DFA4_transition
            )

        self.dfa7 = self.DFA7(
            self, 7,
            eot = self.DFA7_eot,
            eof = self.DFA7_eof,
            min = self.DFA7_min,
            max = self.DFA7_max,
            accept = self.DFA7_accept,
            special = self.DFA7_special,
            transition = self.DFA7_transition
            )




                               
    #@Override
    def reportError(self, e):
        super(OracleNetServicesV3Lexer, self).reportError(e)

        chp = self._state.tokenStartCharPositionInLine
        chl = self._state.tokenStartLine
        lexer_error_start = "{}:{}".format(chl, chp)
            
        if isinstance(e, NoViableAltException):
            raise ValueError('Lexer error at {} => {}:{}, {}'.format(lexer_error_start, e.line, e.charPositionInLine, e))
        elif isinstance(e, (MissingTokenException,MismatchedTokenException)):
            raise ValueError('Lexer error at {} => {}:{}, expecting {}, {}'.format(lexer_error_start, e.line, e.charPositionInLine, e.expecting, e))
        else:
            raise ValueError('Lexer error')



    # $ANTLR start "QUOTED_STRING"
    def mQUOTED_STRING(self, ):

        try:
            _type = QUOTED_STRING
            _channel = DEFAULT_CHANNEL

            # OracleNetServicesV3.g:96:5: ( SINGLE_QUOTE (~ ( SINGLE_QUOTE ) )* SINGLE_QUOTE | DOUBLE_QUOTE (~ ( DOUBLE_QUOTE ) )* DOUBLE_QUOTE )
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 39) :
                alt3 = 1
            elif (LA3_0 == 34) :
                alt3 = 2
            else:
                nvae = NoViableAltException("", 3, 0, self.input)

                raise nvae

            if alt3 == 1:
                # OracleNetServicesV3.g:96:7: SINGLE_QUOTE (~ ( SINGLE_QUOTE ) )* SINGLE_QUOTE
                pass 
                self.mSINGLE_QUOTE()
                # OracleNetServicesV3.g:96:20: (~ ( SINGLE_QUOTE ) )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((0 <= LA1_0 <= 38) or (40 <= LA1_0 <= 65535)) :
                        alt1 = 1


                    if alt1 == 1:
                        # OracleNetServicesV3.g:96:22: ~ ( SINGLE_QUOTE )
                        pass 
                        if (0 <= self.input.LA(1) <= 38) or (40 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop1
                self.mSINGLE_QUOTE()


            elif alt3 == 2:
                # OracleNetServicesV3.g:97:7: DOUBLE_QUOTE (~ ( DOUBLE_QUOTE ) )* DOUBLE_QUOTE
                pass 
                self.mDOUBLE_QUOTE()
                # OracleNetServicesV3.g:97:20: (~ ( DOUBLE_QUOTE ) )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if ((0 <= LA2_0 <= 33) or (35 <= LA2_0 <= 65535)) :
                        alt2 = 1


                    if alt2 == 1:
                        # OracleNetServicesV3.g:97:22: ~ ( DOUBLE_QUOTE )
                        pass 
                        if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop2
                self.mDOUBLE_QUOTE()


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "QUOTED_STRING"



    # $ANTLR start "WORD"
    def mWORD(self, ):

        try:
            _type = WORD
            _channel = DEFAULT_CHANNEL

            # OracleNetServicesV3.g:101:5: ( ( 'A' .. 'Z' | 'a' .. 'z' | '0' .. '9' ) ( 'A' .. 'Z' | 'a' .. 'z' | '0' .. '9' | '<' | '>' | '/' | '.' | ':' | ';' | '-' | '_' | '$' | '+' | '*' | '&' | '!' | '%' | '?' | '@' | '\\\\' . )* )
            # OracleNetServicesV3.g:101:7: ( 'A' .. 'Z' | 'a' .. 'z' | '0' .. '9' ) ( 'A' .. 'Z' | 'a' .. 'z' | '0' .. '9' | '<' | '>' | '/' | '.' | ':' | ';' | '-' | '_' | '$' | '+' | '*' | '&' | '!' | '%' | '?' | '@' | '\\\\' . )*
            pass 
            if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # OracleNetServicesV3.g:105:7: ( 'A' .. 'Z' | 'a' .. 'z' | '0' .. '9' | '<' | '>' | '/' | '.' | ':' | ';' | '-' | '_' | '$' | '+' | '*' | '&' | '!' | '%' | '?' | '@' | '\\\\' . )*
            while True: #loop4
                alt4 = 21
                alt4 = self.dfa4.predict(self.input)
                if alt4 == 1:
                    # OracleNetServicesV3.g:105:9: 'A' .. 'Z'
                    pass 
                    self.matchRange(65, 90)


                elif alt4 == 2:
                    # OracleNetServicesV3.g:106:9: 'a' .. 'z'
                    pass 
                    self.matchRange(97, 122)


                elif alt4 == 3:
                    # OracleNetServicesV3.g:107:9: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                elif alt4 == 4:
                    # OracleNetServicesV3.g:108:9: '<'
                    pass 
                    self.match(60)


                elif alt4 == 5:
                    # OracleNetServicesV3.g:109:9: '>'
                    pass 
                    self.match(62)


                elif alt4 == 6:
                    # OracleNetServicesV3.g:110:9: '/'
                    pass 
                    self.match(47)


                elif alt4 == 7:
                    # OracleNetServicesV3.g:111:9: '.'
                    pass 
                    self.match(46)


                elif alt4 == 8:
                    # OracleNetServicesV3.g:112:9: ':'
                    pass 
                    self.match(58)


                elif alt4 == 9:
                    # OracleNetServicesV3.g:113:9: ';'
                    pass 
                    self.match(59)


                elif alt4 == 10:
                    # OracleNetServicesV3.g:114:9: '-'
                    pass 
                    self.match(45)


                elif alt4 == 11:
                    # OracleNetServicesV3.g:115:9: '_'
                    pass 
                    self.match(95)


                elif alt4 == 12:
                    # OracleNetServicesV3.g:116:9: '$'
                    pass 
                    self.match(36)


                elif alt4 == 13:
                    # OracleNetServicesV3.g:117:9: '+'
                    pass 
                    self.match(43)


                elif alt4 == 14:
                    # OracleNetServicesV3.g:118:9: '*'
                    pass 
                    self.match(42)


                elif alt4 == 15:
                    # OracleNetServicesV3.g:119:9: '&'
                    pass 
                    self.match(38)


                elif alt4 == 16:
                    # OracleNetServicesV3.g:120:9: '!'
                    pass 
                    self.match(33)


                elif alt4 == 17:
                    # OracleNetServicesV3.g:121:9: '%'
                    pass 
                    self.match(37)


                elif alt4 == 18:
                    # OracleNetServicesV3.g:122:9: '?'
                    pass 
                    self.match(63)


                elif alt4 == 19:
                    # OracleNetServicesV3.g:123:9: '@'
                    pass 
                    self.match(64)


                elif alt4 == 20:
                    # OracleNetServicesV3.g:124:9: '\\\\' .
                    pass 
                    self.match(92)
                    self.matchAny()


                else:
                    break #loop4



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WORD"



    # $ANTLR start "LEFT_PAREN"
    def mLEFT_PAREN(self, ):

        try:
            _type = LEFT_PAREN
            _channel = DEFAULT_CHANNEL

            # OracleNetServicesV3.g:129:5: ( '(' )
            # OracleNetServicesV3.g:129:7: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LEFT_PAREN"



    # $ANTLR start "RIGHT_PAREN"
    def mRIGHT_PAREN(self, ):

        try:
            _type = RIGHT_PAREN
            _channel = DEFAULT_CHANNEL

            # OracleNetServicesV3.g:133:5: ( ')' )
            # OracleNetServicesV3.g:133:7: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RIGHT_PAREN"



    # $ANTLR start "EQUALS"
    def mEQUALS(self, ):

        try:
            _type = EQUALS
            _channel = DEFAULT_CHANNEL

            # OracleNetServicesV3.g:137:5: ( '=' )
            # OracleNetServicesV3.g:137:7: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EQUALS"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):

        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # OracleNetServicesV3.g:141:5: ( ',' )
            # OracleNetServicesV3.g:141:7: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "SINGLE_QUOTE"
    def mSINGLE_QUOTE(self, ):

        try:
            _type = SINGLE_QUOTE
            _channel = DEFAULT_CHANNEL

            # OracleNetServicesV3.g:145:5: ( '\\'' )
            # OracleNetServicesV3.g:145:7: '\\''
            pass 
            self.match(39)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SINGLE_QUOTE"



    # $ANTLR start "DOUBLE_QUOTE"
    def mDOUBLE_QUOTE(self, ):

        try:
            _type = DOUBLE_QUOTE
            _channel = DEFAULT_CHANNEL

            # OracleNetServicesV3.g:149:5: ( '\"' )
            # OracleNetServicesV3.g:149:7: '\"'
            pass 
            self.match(34)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOUBLE_QUOTE"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):

        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # OracleNetServicesV3.g:153:5: ( '#' (~ ( '\\n' ) )* )
            # OracleNetServicesV3.g:153:7: '#' (~ ( '\\n' ) )*
            pass 
            self.match(35)
            # OracleNetServicesV3.g:153:11: (~ ( '\\n' ) )*
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((0 <= LA5_0 <= 9) or (11 <= LA5_0 <= 65535)) :
                    alt5 = 1


                if alt5 == 1:
                    # OracleNetServicesV3.g:153:13: ~ ( '\\n' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop5
            #action start
            _channel=HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "WHITESPACE"
    def mWHITESPACE(self, ):

        try:
            _type = WHITESPACE
            _channel = DEFAULT_CHANNEL

            # OracleNetServicesV3.g:157:5: ( ( '\\t' | ' ' ) )
            # OracleNetServicesV3.g:157:7: ( '\\t' | ' ' )
            pass 
            if self.input.LA(1) == 9 or self.input.LA(1) == 32:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            #action start
            _channel=HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHITESPACE"



    # $ANTLR start "NEWLINE"
    def mNEWLINE(self, ):

        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            # OracleNetServicesV3.g:163:5: ( ( '\\r' )? '\\n' )
            # OracleNetServicesV3.g:163:7: ( '\\r' )? '\\n'
            pass 
            # OracleNetServicesV3.g:163:7: ( '\\r' )?
            alt6 = 2
            LA6_0 = self.input.LA(1)

            if (LA6_0 == 13) :
                alt6 = 1
            if alt6 == 1:
                # OracleNetServicesV3.g:163:9: '\\r'
                pass 
                self.match(13)



            self.match(10)
            #action start
            _channel=HIDDEN;
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NEWLINE"



    def mTokens(self):
        # OracleNetServicesV3.g:1:8: ( QUOTED_STRING | WORD | LEFT_PAREN | RIGHT_PAREN | EQUALS | COMMA | SINGLE_QUOTE | DOUBLE_QUOTE | COMMENT | WHITESPACE | NEWLINE )
        alt7 = 11
        alt7 = self.dfa7.predict(self.input)
        if alt7 == 1:
            # OracleNetServicesV3.g:1:10: QUOTED_STRING
            pass 
            self.mQUOTED_STRING()


        elif alt7 == 2:
            # OracleNetServicesV3.g:1:24: WORD
            pass 
            self.mWORD()


        elif alt7 == 3:
            # OracleNetServicesV3.g:1:29: LEFT_PAREN
            pass 
            self.mLEFT_PAREN()


        elif alt7 == 4:
            # OracleNetServicesV3.g:1:40: RIGHT_PAREN
            pass 
            self.mRIGHT_PAREN()


        elif alt7 == 5:
            # OracleNetServicesV3.g:1:52: EQUALS
            pass 
            self.mEQUALS()


        elif alt7 == 6:
            # OracleNetServicesV3.g:1:59: COMMA
            pass 
            self.mCOMMA()


        elif alt7 == 7:
            # OracleNetServicesV3.g:1:65: SINGLE_QUOTE
            pass 
            self.mSINGLE_QUOTE()


        elif alt7 == 8:
            # OracleNetServicesV3.g:1:78: DOUBLE_QUOTE
            pass 
            self.mDOUBLE_QUOTE()


        elif alt7 == 9:
            # OracleNetServicesV3.g:1:91: COMMENT
            pass 
            self.mCOMMENT()


        elif alt7 == 10:
            # OracleNetServicesV3.g:1:99: WHITESPACE
            pass 
            self.mWHITESPACE()


        elif alt7 == 11:
            # OracleNetServicesV3.g:1:110: NEWLINE
            pass 
            self.mNEWLINE()







    # lookup tables for DFA #4

    DFA4_eot = DFA.unpack(
        u"\1\1\25\uffff"
        )

    DFA4_eof = DFA.unpack(
        u"\26\uffff"
        )

    DFA4_min = DFA.unpack(
        u"\1\41\25\uffff"
        )

    DFA4_max = DFA.unpack(
        u"\1\172\25\uffff"
        )

    DFA4_accept = DFA.unpack(
        u"\1\uffff\1\25\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\12\1\13\1"
        u"\14\1\15\1\16\1\17\1\20\1\21\1\22\1\23\1\24"
        )

    DFA4_special = DFA.unpack(
        u"\26\uffff"
        )

            
    DFA4_transition = [
        DFA.unpack(u"\1\21\2\uffff\1\15\1\22\1\20\3\uffff\1\17\1\16\1\uffff"
        u"\1\13\1\10\1\7\12\4\1\11\1\12\1\5\1\uffff\1\6\1\23\1\24\32\2\1"
        u"\uffff\1\25\2\uffff\1\14\1\uffff\32\3"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #4

    class DFA4(DFA):
        pass


    # lookup tables for DFA #7

    DFA7_eot = DFA.unpack(
        u"\1\uffff\1\13\1\15\13\uffff"
        )

    DFA7_eof = DFA.unpack(
        u"\16\uffff"
        )

    DFA7_min = DFA.unpack(
        u"\1\11\2\0\13\uffff"
        )

    DFA7_max = DFA.unpack(
        u"\1\172\2\uffff\13\uffff"
        )

    DFA7_accept = DFA.unpack(
        u"\3\uffff\1\2\1\3\1\4\1\5\1\6\1\11\1\12\1\13\1\7\1\1\1\10"
        )

    DFA7_special = DFA.unpack(
        u"\1\uffff\1\0\1\1\13\uffff"
        )

            
    DFA7_transition = [
        DFA.unpack(u"\1\11\1\12\2\uffff\1\12\22\uffff\1\11\1\uffff\1\2\1"
        u"\10\3\uffff\1\1\1\4\1\5\2\uffff\1\7\3\uffff\12\3\3\uffff\1\6\3"
        u"\uffff\32\3\6\uffff\32\3"),
        DFA.unpack(u"\0\14"),
        DFA.unpack(u"\0\14"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #7

    class DFA7(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA7_1 = input.LA(1)

                s = -1
                if ((0 <= LA7_1 <= 65535)):
                    s = 12

                else:
                    s = 11

                if s >= 0:
                    return s
            elif s == 1: 
                LA7_2 = input.LA(1)

                s = -1
                if ((0 <= LA7_2 <= 65535)):
                    s = 12

                else:
                    s = 13

                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 7, _s, input)
            self_.error(nvae)
            raise nvae
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from .antlr3.main import LexerMain
    main = LexerMain(OracleNetServicesV3Lexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
