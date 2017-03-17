# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib/python2.7/dist-packages/PyQt4/QtCore.so
# by generator 1.143
# no doc

# imports
import sip as __sip


class QLocale(): # skipped bases: <type 'sip.simplewrapper'>
    """
    QLocale()
    QLocale(QString)
    QLocale(QLocale.Language, QLocale.Country country=QLocale.AnyCountry)
    QLocale(QLocale)
    QLocale(QLocale.Language, QLocale.Script, QLocale.Country)
    """
    def amText(self): # real signature unknown; restored from __doc__
        """ QLocale.amText() -> QString """
        return QString

    def bcp47Name(self): # real signature unknown; restored from __doc__
        """ QLocale.bcp47Name() -> QString """
        return QString

    def c(self): # real signature unknown; restored from __doc__
        """ QLocale.c() -> QLocale """
        return QLocale

    def countriesForLanguage(self, QLocale_Language): # real signature unknown; restored from __doc__
        """ QLocale.countriesForLanguage(QLocale.Language) -> list-of-QLocale.Country """
        pass

    def country(self): # real signature unknown; restored from __doc__
        """ QLocale.country() -> QLocale.Country """
        pass

    def countryToString(self, QLocale_Country): # real signature unknown; restored from __doc__
        """ QLocale.countryToString(QLocale.Country) -> QString """
        return QString

    def createSeparatedList(self, QStringList): # real signature unknown; restored from __doc__
        """ QLocale.createSeparatedList(QStringList) -> QString """
        return QString

    def currencySymbol(self, QLocale_CurrencySymbolFormat_format=None): # real signature unknown; restored from __doc__
        """ QLocale.currencySymbol(QLocale.CurrencySymbolFormat format=QLocale.CurrencySymbol) -> QString """
        return QString

    def dateFormat(self, QLocale_FormatType_format=None): # real signature unknown; restored from __doc__
        """ QLocale.dateFormat(QLocale.FormatType format=QLocale.LongFormat) -> QString """
        return QString

    def dateTimeFormat(self, QLocale_FormatType_format=None): # real signature unknown; restored from __doc__
        """ QLocale.dateTimeFormat(QLocale.FormatType format=QLocale.LongFormat) -> QString """
        return QString

    def dayName(self, p_int, QLocale_FormatType_format=None): # real signature unknown; restored from __doc__
        """ QLocale.dayName(int, QLocale.FormatType format=QLocale.LongFormat) -> QString """
        return QString

    def decimalPoint(self): # real signature unknown; restored from __doc__
        """ QLocale.decimalPoint() -> QChar """
        return QChar

    def exponential(self): # real signature unknown; restored from __doc__
        """ QLocale.exponential() -> QChar """
        return QChar

    def firstDayOfWeek(self): # real signature unknown; restored from __doc__
        """ QLocale.firstDayOfWeek() -> Qt.DayOfWeek """
        pass

    def groupSeparator(self): # real signature unknown; restored from __doc__
        """ QLocale.groupSeparator() -> QChar """
        return QChar

    def language(self): # real signature unknown; restored from __doc__
        """ QLocale.language() -> QLocale.Language """
        pass

    def languageToString(self, QLocale_Language): # real signature unknown; restored from __doc__
        """ QLocale.languageToString(QLocale.Language) -> QString """
        return QString

    def matchingLocales(self, QLocale_Language, QLocale_Script, QLocale_Country): # real signature unknown; restored from __doc__
        """ QLocale.matchingLocales(QLocale.Language, QLocale.Script, QLocale.Country) -> list-of-QLocale """
        pass

    def measurementSystem(self): # real signature unknown; restored from __doc__
        """ QLocale.measurementSystem() -> QLocale.MeasurementSystem """
        pass

    def monthName(self, p_int, QLocale_FormatType_format=None): # real signature unknown; restored from __doc__
        """ QLocale.monthName(int, QLocale.FormatType format=QLocale.LongFormat) -> QString """
        return QString

    def name(self): # real signature unknown; restored from __doc__
        """ QLocale.name() -> QString """
        return QString

    def nativeCountryName(self): # real signature unknown; restored from __doc__
        """ QLocale.nativeCountryName() -> QString """
        return QString

    def nativeLanguageName(self): # real signature unknown; restored from __doc__
        """ QLocale.nativeLanguageName() -> QString """
        return QString

    def negativeSign(self): # real signature unknown; restored from __doc__
        """ QLocale.negativeSign() -> QChar """
        return QChar

    def numberOptions(self): # real signature unknown; restored from __doc__
        """ QLocale.numberOptions() -> QLocale.NumberOptions """
        pass

    def percent(self): # real signature unknown; restored from __doc__
        """ QLocale.percent() -> QChar """
        return QChar

    def pmText(self): # real signature unknown; restored from __doc__
        """ QLocale.pmText() -> QString """
        return QString

    def positiveSign(self): # real signature unknown; restored from __doc__
        """ QLocale.positiveSign() -> QChar """
        return QChar

    def quoteString(self, QString, QLocale_QuotationStyle_style=None): # real signature unknown; restored from __doc__
        """ QLocale.quoteString(QString, QLocale.QuotationStyle style=QLocale.StandardQuotation) -> QString """
        return QString

    def script(self): # real signature unknown; restored from __doc__
        """ QLocale.script() -> QLocale.Script """
        pass

    def scriptToString(self, QLocale_Script): # real signature unknown; restored from __doc__
        """ QLocale.scriptToString(QLocale.Script) -> QString """
        return QString

    def setDefault(self, QLocale): # real signature unknown; restored from __doc__
        """ QLocale.setDefault(QLocale) """
        pass

    def setNumberOptions(self, QLocale_NumberOptions): # real signature unknown; restored from __doc__
        """ QLocale.setNumberOptions(QLocale.NumberOptions) """
        pass

    def standaloneDayName(self, p_int, QLocale_FormatType_format=None): # real signature unknown; restored from __doc__
        """ QLocale.standaloneDayName(int, QLocale.FormatType format=QLocale.LongFormat) -> QString """
        return QString

    def standaloneMonthName(self, p_int, QLocale_FormatType_format=None): # real signature unknown; restored from __doc__
        """ QLocale.standaloneMonthName(int, QLocale.FormatType format=QLocale.LongFormat) -> QString """
        return QString

    def system(self): # real signature unknown; restored from __doc__
        """ QLocale.system() -> QLocale """
        return QLocale

    def textDirection(self): # real signature unknown; restored from __doc__
        """ QLocale.textDirection() -> Qt.LayoutDirection """
        pass

    def timeFormat(self, QLocale_FormatType_format=None): # real signature unknown; restored from __doc__
        """ QLocale.timeFormat(QLocale.FormatType format=QLocale.LongFormat) -> QString """
        return QString

    def toCurrencyString(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QLocale.toCurrencyString(int, QString symbol=QString()) -> QString
        QLocale.toCurrencyString(float, QString symbol=QString()) -> QString
        QLocale.toCurrencyString(int, QString symbol=QString()) -> QString
        QLocale.toCurrencyString(int, QString symbol=QString()) -> QString
        """
        pass

    def toDate(self, QString, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QLocale.toDate(QString, QLocale.FormatType format=QLocale.LongFormat) -> QDate
        QLocale.toDate(QString, QString) -> QDate
        """
        return QDate

    def toDateTime(self, QString, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QLocale.toDateTime(QString, QLocale.FormatType format=QLocale.LongFormat) -> QDateTime
        QLocale.toDateTime(QString, QString) -> QDateTime
        """
        return QDateTime

    def toDouble(self, QString): # real signature unknown; restored from __doc__
        """ QLocale.toDouble(QString) -> (float, bool) """
        pass

    def toFloat(self, QString): # real signature unknown; restored from __doc__
        """ QLocale.toFloat(QString) -> (float, bool) """
        pass

    def toInt(self, QString, int_base=0): # real signature unknown; restored from __doc__
        """ QLocale.toInt(QString, int base=0) -> (int, bool) """
        pass

    def toLongLong(self, QString, int_base=0): # real signature unknown; restored from __doc__
        """ QLocale.toLongLong(QString, int base=0) -> (int, bool) """
        pass

    def toLower(self, QString): # real signature unknown; restored from __doc__
        """ QLocale.toLower(QString) -> QString """
        return QString

    def toShort(self, QString, int_base=0): # real signature unknown; restored from __doc__
        """ QLocale.toShort(QString, int base=0) -> (int, bool) """
        pass

    def toString(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QLocale.toString(int) -> QString
        QLocale.toString(float, str format='g', int precision=6) -> QString
        QLocale.toString(int) -> QString
        QLocale.toString(int) -> QString
        QLocale.toString(QDateTime, QString) -> QString
        QLocale.toString(QDateTime, QLocale.FormatType format=QLocale.LongFormat) -> QString
        QLocale.toString(QDate, QString) -> QString
        QLocale.toString(QDate, QLocale.FormatType format=QLocale.LongFormat) -> QString
        QLocale.toString(QTime, QString) -> QString
        QLocale.toString(QTime, QLocale.FormatType format=QLocale.LongFormat) -> QString
        """
        return QString

    def toTime(self, QString, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        QLocale.toTime(QString, QLocale.FormatType format=QLocale.LongFormat) -> QTime
        QLocale.toTime(QString, QString) -> QTime
        """
        return QTime

    def toUInt(self, QString, int_base=0): # real signature unknown; restored from __doc__
        """ QLocale.toUInt(QString, int base=0) -> (int, bool) """
        pass

    def toULongLong(self, QString, int_base=0): # real signature unknown; restored from __doc__
        """ QLocale.toULongLong(QString, int base=0) -> (int, bool) """
        pass

    def toUpper(self, QString): # real signature unknown; restored from __doc__
        """ QLocale.toUpper(QString) -> QString """
        return QString

    def toUShort(self, QString, int_base=0): # real signature unknown; restored from __doc__
        """ QLocale.toUShort(QString, int base=0) -> (int, bool) """
        pass

    def uiLanguages(self): # real signature unknown; restored from __doc__
        """ QLocale.uiLanguages() -> QStringList """
        return QStringList

    def weekdays(self): # real signature unknown; restored from __doc__
        """ QLocale.weekdays() -> list-of-Qt.DayOfWeek """
        pass

    def zeroDigit(self): # real signature unknown; restored from __doc__
        """ QLocale.zeroDigit() -> QChar """
        return QChar

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Abkhazian = 2
    Afan = 3
    Afar = 4
    Afghanistan = 1
    Afrikaans = 5
    Aghem = 216
    Akan = 146
    Albania = 2
    Albanian = 6
    Algeria = 3
    AlternateQuotation = 1
    AmericanSamoa = 4
    Amharic = 7
    Andorra = 5
    Angola = 6
    Anguilla = 7
    Antarctica = 8
    AntiguaAndBarbuda = 9
    AnyCountry = 0
    AnyLanguage = 0
    AnyScript = 0
    Arabic = 8
    ArabicScript = 1
    Argentina = 10
    Armenia = 11
    Armenian = 9
    Aruba = 12
    Assamese = 10
    Asu = 205
    Atsam = 156
    Australia = 13
    Austria = 14
    Aymara = 11
    Azerbaijan = 15
    Azerbaijani = 12
    Bafia = 222
    Bahamas = 16
    Bahrain = 17
    Bambara = 188
    Bangladesh = 18
    Barbados = 19
    Basaa = 217
    Bashkir = 13
    Basque = 14
    Belarus = 20
    Belgium = 21
    Belize = 22
    Bemba = 195
    Bena = 186
    Bengali = 15
    Benin = 23
    Bermuda = 24
    Bhutan = 25
    Bhutani = 16
    Bihari = 17
    Bislama = 18
    Blin = 152
    Bodo = 215
    Bolivia = 26
    BosniaAndHerzegowina = 27
    Bosnian = 142
    Botswana = 28
    BouvetIsland = 29
    Brazil = 30
    Breton = 19
    BritishIndianOceanTerritory = 31
    BritishVirginIslands = 233
    BruneiDarussalam = 32
    Bulgaria = 33
    Bulgarian = 20
    BurkinaFaso = 34
    Burmese = 21
    Burundi = 35
    Byelorussian = 22
    C = 1
    Cambodia = 36
    Cambodian = 23
    Cameroon = 37
    Canada = 38
    CapeVerde = 39
    Catalan = 24
    CaymanIslands = 40
    CentralAfricanRepublic = 41
    CentralMoroccoTamazight = 212
    Chad = 42
    Cherokee = 190
    Chewa = 165
    Chiga = 211
    Chile = 43
    China = 44
    Chinese = 25
    ChristmasIsland = 45
    CocosIslands = 46
    Colognian = 201
    Colombia = 47
    Comoros = 48
    CongoSwahili = 230
    CookIslands = 51
    Cornish = 145
    Corsican = 26
    CostaRica = 52
    Croatia = 54
    Croatian = 27
    Cuba = 55
    CurrencyDisplayName = 2
    CurrencyIsoCode = 0
    CurrencySymbol = 1
    Cyprus = 56
    CyrillicScript = 2
    Czech = 28
    CzechRepublic = 57
    Danish = 29
    DemocraticRepublicOfCongo = 49
    DemocraticRepublicOfKorea = 113
    Denmark = 58
    DeseretScript = 3
    Divehi = 143
    Djibouti = 59
    Dominica = 60
    DominicanRepublic = 61
    Duala = 219
    Dutch = 30
    EastTimor = 62
    Ecuador = 63
    Egypt = 64
    ElSalvador = 65
    Embu = 189
    English = 31
    EquatorialGuinea = 66
    Eritrea = 67
    Esperanto = 32
    Estonia = 68
    Estonian = 33
    Ethiopia = 69
    Ewe = 161
    Ewondo = 221
    FalklandIslands = 70
    FaroeIslands = 71
    Faroese = 34
    FijiCountry = 72
    FijiLanguage = 35
    Filipino = 166
    Finland = 73
    Finnish = 36
    France = 74
    French = 37
    FrenchGuiana = 76
    FrenchPolynesia = 77
    FrenchSouthernTerritories = 78
    Frisian = 38
    Friulian = 159
    Fulah = 177
    Ga = 148
    Gabon = 79
    Gaelic = 39
    Galician = 40
    Gambia = 80
    Ganda = 194
    Geez = 153
    Georgia = 81
    Georgian = 41
    German = 42
    Germany = 82
    Ghana = 83
    Gibraltar = 84
    Greece = 85
    Greek = 43
    Greenland = 86
    Greenlandic = 44
    Grenada = 87
    Guadeloupe = 88
    Guam = 89
    Guarani = 45
    Guatemala = 90
    Guinea = 91
    GuineaBissau = 92
    Gujarati = 46
    GurmukhiScript = 4
    Gusii = 175
    Guyana = 93
    Haiti = 94
    Hausa = 47
    Hawaiian = 163
    HeardAndMcDonaldIslands = 95
    Hebrew = 48
    Hindi = 49
    Honduras = 96
    HongKong = 97
    Hungarian = 50
    Hungary = 98
    Iceland = 99
    Icelandic = 51
    Igbo = 149
    ImperialSystem = 1
    India = 100
    Indonesia = 101
    Indonesian = 52
    Interlingua = 53
    Interlingue = 54
    Inuktitut = 55
    Inupiak = 56
    Iran = 102
    Iraq = 103
    Ireland = 104
    Irish = 57
    Israel = 105
    Italian = 58
    Italy = 106
    IvoryCoast = 53
    Jamaica = 107
    Japan = 108
    Japanese = 59
    Javanese = 60
    Jju = 158
    JolaFonyi = 220
    Jordan = 109
    Kabuverdianu = 196
    Kabyle = 184
    Kalenjin = 198
    Kamba = 150
    Kannada = 61
    Kashmiri = 62
    Kazakh = 63
    Kazakhstan = 110
    Kenya = 111
    Kikuyu = 178
    Kinyarwanda = 64
    Kirghiz = 65
    Kiribati = 112
    Konkani = 147
    Korean = 66
    Koro = 154
    KoyraboroSenni = 213
    KoyraChiini = 208
    Kpelle = 169
    Kurdish = 67
    Kurundi = 68
    Kuwait = 115
    Kwasio = 226
    Kyrgyzstan = 116
    Langi = 193
    Lao = 117
    Laothian = 69
    LastCountry = 246
    LastLanguage = 234
    Latin = 70
    LatinAmericaAndTheCaribbean = 246
    LatinScript = 7
    Latvia = 118
    Latvian = 71
    Lebanon = 119
    Lesotho = 120
    Liberia = 121
    LibyanArabJamahiriya = 122
    Liechtenstein = 123
    Lingala = 72
    Lithuania = 124
    Lithuanian = 73
    LongFormat = 0
    LowGerman = 170
    LubaKatanga = 223
    Luo = 210
    Luxembourg = 125
    Luyia = 204
    Macau = 126
    Macedonia = 127
    Macedonian = 74
    Machame = 200
    Madagascar = 128
    MakhuwaMeetto = 224
    Makonde = 192
    Malagasy = 75
    Malawi = 129
    Malay = 76
    Malayalam = 77
    Malaysia = 130
    Maldives = 131
    Mali = 132
    Malta = 133
    Maltese = 78
    Manx = 144
    Maori = 79
    Marathi = 80
    MarshallIslands = 134
    Martinique = 135
    Masai = 202
    Mauritania = 136
    Mauritius = 137
    Mayotte = 138
    Meru = 197
    MetricSystem = 0
    MetropolitanFrance = 75
    Mexico = 139
    Micronesia = 140
    Moldavian = 81
    Moldova = 141
    Monaco = 142
    Mongolia = 143
    Mongolian = 82
    MongolianScript = 8
    Montenegro = 242
    Montserrat = 144
    Morisyen = 191
    Morocco = 145
    Mozambique = 146
    Mundang = 225
    Myanmar = 147
    Nama = 199
    Namibia = 148
    NarrowFormat = 2
    NauruCountry = 149
    NauruLanguage = 83
    Nepal = 150
    Nepali = 84
    Netherlands = 151
    NetherlandsAntilles = 152
    NewCaledonia = 153
    NewZealand = 154
    Nicaragua = 155
    Niger = 156
    Nigeria = 157
    Niue = 158
    NorfolkIsland = 159
    NorthernMarianaIslands = 160
    NorthernSami = 173
    NorthernSotho = 172
    NorthNdebele = 181
    Norway = 161
    Norwegian = 85
    NorwegianBokmal = 85
    NorwegianNynorsk = 141
    Nuer = 227
    Nyankole = 185
    Nynorsk = 141
    Occitan = 86
    Oman = 162
    OmitGroupSeparator = 1
    Oriya = 87
    Pakistan = 163
    Palau = 164
    PalestinianTerritory = 165
    Panama = 166
    PapuaNewGuinea = 167
    Paraguay = 168
    Pashto = 88
    PeoplesRepublicOfCongo = 50
    Persian = 89
    Peru = 169
    Philippines = 170
    Pitcairn = 171
    Poland = 172
    Polish = 90
    Portugal = 173
    Portuguese = 91
    PuertoRico = 174
    Punjabi = 92
    Qatar = 175
    Quechua = 93
    RejectGroupSeparator = 2
    RepublicOfKorea = 114
    Reunion = 176
    RhaetoRomance = 94
    Romania = 177
    Romanian = 95
    Rombo = 182
    Rundi = 68
    Russian = 96
    RussianFederation = 178
    Rwa = 209
    Rwanda = 179
    Saho = 207
    SaintBarthelemy = 244
    SaintKittsAndNevis = 180
    SaintMartin = 245
    Sakha = 228
    Samburu = 179
    Samoa = 183
    Samoan = 97
    Sangho = 98
    Sangu = 229
    SanMarino = 184
    Sanskrit = 99
    SaoTomeAndPrincipe = 185
    SaudiArabia = 186
    Sena = 180
    Senegal = 187
    Serbia = 243
    SerbiaAndMontenegro = 241
    Serbian = 100
    SerboCroatian = 101
    Sesotho = 102
    Setswana = 103
    Seychelles = 188
    Shambala = 214
    Shona = 104
    ShortFormat = 1
    SichuanYi = 168
    Sidamo = 155
    SierraLeone = 189
    SimplifiedChineseScript = 5
    SimplifiedHanScript = 5
    Sindhi = 105
    Singapore = 190
    Singhalese = 106
    Siswati = 107
    Slovak = 108
    Slovakia = 191
    Slovenia = 192
    Slovenian = 109
    Soga = 203
    SolomonIslands = 193
    Somali = 110
    Somalia = 194
    SouthAfrica = 195
    SouthGeorgiaAndTheSouthSandwichIslands = 196
    SouthNdebele = 171
    Spain = 197
    Spanish = 111
    SriLanka = 198
    StandardQuotation = 0
    StHelena = 199
    StLucia = 181
    StPierreAndMiquelon = 200
    StVincentAndTheGrenadines = 182
    Sudan = 201
    Sundanese = 112
    Suriname = 202
    SvalbardAndJanMayenIslands = 203
    Swahili = 113
    Swaziland = 204
    Sweden = 205
    Swedish = 114
    SwissGerman = 167
    Switzerland = 206
    Syriac = 151
    SyrianArabRepublic = 207
    Tachelhit = 183
    Tagalog = 115
    Taita = 176
    Taiwan = 208
    Tajik = 116
    Tajikistan = 209
    Tamil = 117
    Tanzania = 210
    Taroko = 174
    Tasawaq = 231
    Tatar = 118
    Telugu = 119
    Teso = 206
    Thai = 120
    Thailand = 211
    Tibetan = 121
    TifinaghScript = 9
    Tigre = 157
    Tigrinya = 122
    Togo = 212
    Tokelau = 213
    TongaCountry = 214
    TongaLanguage = 123
    TraditionalChineseScript = 6
    TraditionalHanScript = 6
    TrinidadAndTobago = 215
    Tsonga = 124
    Tunisia = 216
    Turkey = 217
    Turkish = 125
    Turkmen = 126
    Turkmenistan = 218
    TurksAndCaicosIslands = 219
    Tuvalu = 220
    Twi = 127
    Tyap = 164
    Uganda = 221
    Uigur = 128
    Ukraine = 222
    Ukrainian = 129
    UnitedArabEmirates = 223
    UnitedKingdom = 224
    UnitedStates = 225
    UnitedStatesMinorOutlyingIslands = 226
    Urdu = 130
    Uruguay = 227
    USVirginIslands = 234
    Uzbek = 131
    Uzbekistan = 228
    Vai = 232
    Vanuatu = 229
    VaticanCityState = 230
    Venda = 160
    Venezuela = 231
    VietNam = 232
    Vietnamese = 132
    Volapuk = 133
    Vunjo = 187
    Walamo = 162
    WallisAndFutunaIslands = 235
    Walser = 233
    Welsh = 134
    WesternSahara = 236
    Wolof = 135
    Xhosa = 136
    Yangben = 234
    Yemen = 237
    Yiddish = 137
    Yoruba = 138
    Yugoslavia = 238
    Zambia = 239
    Zarma = 218
    Zhuang = 139
    Zimbabwe = 240
    Zulu = 140


