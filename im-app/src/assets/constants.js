export const MainConstants = Object.freeze({
    REQUESTADRESS: "http://localhost",
    PORT: "5000",
    LOGSTRING_VALIDATION: /^\s*(\s*<\s*(([a-zA-Z]+\s*,\s*)*[a-zA-Z]+\s*)>+\s*\d*\s*;)+\s*$/,
    SOCKETPATH: '~/projectprocessmining/pythonproject/imviz.sock'
});

export const BuildConstants = Object.freeze({
    REQUESTADRESSBASE: MainConstants.REQUESTADRESS + ":" + MainConstants.PORT
});
