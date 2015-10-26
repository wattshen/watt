function pwdLevel(value) {
    var pattern_1 = /^.*([\W_])+.*$/i;
    var pattern_2 = /^.*([a-zA-Z])+.*$/i;
    var pattern_3 = /^.*([0-9])+.*$/i;
    var level = 0;
    if (value.length > 10) {
        level++;
    }
    if (pattern_1.test(value)) {
        level++;
    }
    if (pattern_2.test(value)) {
        level++;
    }
    if (pattern_3.test(value)) {
        level++;
    }
    if (level > 3) {
        level = 3;
    }
    return level;
}

var weakPwdArray = ["123456","123456789","111111","5201314","12345678","123123","password","1314520","123321","7758521","1234567","5211314","666666","520520","woaini","520131","11111111","888888","hotmail.com","112233","123654","654321","1234567890","a123456","88888888","163.com","000000","yahoo.com.cn","sohu.com","yahoo.cn","111222tianya","163.COM","tom.com","139.com","wangyut2","pp.com","yahoo.com","147258369","123123123","147258","987654321","100200","zxcvbnm","123456a","521521","7758258","111222","110110","1314521","11111111","12345678","a321654","111111","123123","5201314","00000000","q123456","123123123","aaaaaa","a123456789","qq123456","11112222","woaini1314","a123123","a111111","123321","a5201314","z123456","liuchang","a000000","1314520","asd123","88888888","1234567890","7758521","1234567","woaini520","147258369","123456789a","woaini123","q1q1q1q1","a12345678","qwe123","123456q","121212","asdasd","999999","1111111","123698745","137900","159357","iloveyou","222222","31415926","123456","111111","123456789","123123","9958123","woaini521","5201314","18n28n24a5","abc123","password","123qwe","123456789","12345678","11111111","dearbook","00000000","123123123","1234567890","88888888","111111111","147258369","987654321","aaaaaaaa","1111111111","66666666","a123456789","11223344","1qaz2wsx","xiazhili","789456123","password","87654321","qqqqqqqq","000000000","qwertyuiop","qq123456","iloveyou","31415926","12344321","0000000000","asdfghjkl","1q2w3e4r","123456abc","0123456789","123654789","12121212","qazwsxedc","abcd1234","12341234","110110110","asdasdasd","123456","22222222","123321123","abc123456","a12345678","123456123","a1234567","1234qwer","qwertyui","123456789a","qq.com","369369","163.com","ohwe1zvq","xiekai1121","19860210","1984130","81251310","502058","162534","690929","601445","1814325","as1230","zz123456","280213676","198773","4861111","328658","19890608","198428","880126","6516415","111213","195561","780525","6586123","caonima99","168816","123654987","qq776491","hahabaobao","198541","540707","leqing123","5403693","123456","123456789","111111","5201314","123123","12345678","1314520","123321","7758521","1234567","5211314","520520","woaini","520131","666666","RAND#a#8","hotmail.com","112233","123654","888888","654321","1234567890","a123456"];

function verc() {
    $("#JD_Verification1").click();
}

var validateRegExp = {
    decmal: "^([+-]?)\\d*\\.\\d+$", //������
    decmal1: "^[1-9]\\d*.\\d*|0.\\d*[1-9]\\d*$", //��������
    decmal2: "^-([1-9]\\d*.\\d*|0.\\d*[1-9]\\d*)$", //��������
    decmal3: "^-?([1-9]\\d*.\\d*|0.\\d*[1-9]\\d*|0?.0+|0)$", //������
    decmal4: "^[1-9]\\d*.\\d*|0.\\d*[1-9]\\d*|0?.0+|0$", //�Ǹ����������������� + 0��
    decmal5: "^(-([1-9]\\d*.\\d*|0.\\d*[1-9]\\d*))|0?.0+|0$", //�������������������� + 0��
    intege: "^-?[1-9]\\d*$", //����
    intege1: "^[1-9]\\d*$", //������
    intege2: "^-[1-9]\\d*$", //������
    num: "^([+-]?)\\d*\\.?\\d+$", //����
    num1: "^[1-9]\\d*|0$", //������������ + 0��
    num2: "^-[1-9]\\d*|0$", //������������ + 0��
    ascii: "^[\\x00-\\xFF]+$", //��ACSII�ַ�
    chinese: "^[\\u4e00-\\u9fa5]+$", //������
    color: "^[a-fA-F0-9]{6}$", //��ɫ
    date: "^\\d{4}(\\-|\\/|\.)\\d{1,2}\\1\\d{1,2}$", //����
    email: "^\\w+((-\\w+)|(\\.\\w+))*\\@[A-Za-z0-9]+((\\.|-)[A-Za-z0-9]+)*\\.[A-Za-z0-9]+$", //�ʼ�
    idcard: "^[1-9]([0-9]{14}|[0-9]{17})$", //���֤
    ip4: "^(25[0-5]|2[0-4]\\d|[0-1]\\d{2}|[1-9]?\\d)\\.(25[0-5]|2[0-4]\\d|[0-1]\\d{2}|[1-9]?\\d)\\.(25[0-5]|2[0-4]\\d|[0-1]\\d{2}|[1-9]?\\d)\\.(25[0-5]|2[0-4]\\d|[0-1]\\d{2}|[1-9]?\\d)$", //ip��ַ
    letter: "^[A-Za-z]+$", //��ĸ
    letter_l: "^[a-z]+$", //Сд��ĸ
    letter_u: "^[A-Z]+$", //��д��ĸ
    mobile: "^0?(13|15|18|14)[0-9]{9}$", //�ֻ�
    notempty: "^\\S+$", //�ǿ�
    password: "^.*[A-Za-z0-9\\w_-]+.*$", //����
    fullNumber: "^[0-9]+$", //����
    picture: "(.*)\\.(jpg|bmp|gif|ico|pcx|jpeg|tif|png|raw|tga)$", //ͼƬ
    qq: "^[1-9]*[1-9][0-9]*$", //QQ����
    rar: "(.*)\\.(rar|zip|7zip|tgz)$", //ѹ���ļ�
    tel: "^[0-9\-()����]{7,18}$", //�绰����ĺ���(������֤��������,��������,�ֻ���)
    url: "^http[s]?:\\/\\/([\\w-]+\\.)+[\\w-]+([\\w-./?%&=]*)?$", //url
    username: "^[A-Za-z0-9_\\-\\u4e00-\\u9fa5]+$", //����
    deptname: "^[A-Za-z0-9_()����\\-\\u4e00-\\u9fa5]+$", //��λ��
    zipcode: "^\\d{6}$", //�ʱ�
    realname: "^[A-Za-z\\u4e00-\\u9fa5]+$", // ��ʵ����
    companyname: "^[A-Za-z0-9_()����\\-\\u4e00-\\u9fa5]+$",
    companyaddr: "^[A-Za-z0-9_()����\\#\\-\\u4e00-\\u9fa5]+$",
    companysite: "^http[s]?:\\/\\/([\\w-]+\\.)+[\\w-]+([\\w-./?%&#=]*)?$"
};
//������
(function ($) {
    $.fn.jdValidate = function (option, callback, def) {
        var ele = this;
        var id = ele.attr("id");
        var type = ele.attr("type");
        var rel = ele.attr("rel");
        var _onFocus = $("#" + id + validateSettings.onFocus.container);
        var _succeed = $("#" + id + validateSettings.succeed.container);
        var _isNull = $("#" + id + validateSettings.isNull.container);
        var _error = $("#" + id + validateSettings.error.container);
        if (def == true) {
            var str = ele.val();
            var tag = ele.attr("sta");
            if (str == "" || str == "-1") {
                validateSettings.isNull.run({
                    prompts: option,
                    element: ele,
                    isNullEle: _isNull,
                    succeedEle: _succeed
                }, option.isNull);
            } else if (tag == 1 || tag == 2) {
                return;
            } else {
                callback({
                    prompts: option,
                    element: ele,
                    value: str,
                    errorEle: _error,
                    succeedEle: _succeed
                });
            }
        } else {
            if (typeof def == "string") {
                ele.val(def);
            }
            if (type == "checkbox" || type == "radio") {
                if (ele.attr("checked") == true) {
                    ele.attr("sta", validateSettings.succeed.state);
                }
            }
            switch (type) {
                case "text":
                case "password":
                    ele.bind("focus", function () {
                        var str = ele.val();
                        if (str == def) {
                            ele.val("");
                        }
                        validateSettings.onFocus.run({
                            prompts: option,
                            element: ele,
                            value: str,
                            onFocusEle: _onFocus,
                            succeedEle: _succeed
                        }, option.onFocus, option.onFocusExpand);
                    })
                        .bind("blur", function () {
                            var str = ele.val();
                            if (str == "") {
                                ele.val(def);
                            }
                            if (validateRules.isNull(str)) {
                                validateSettings.isNull.run({
                                    prompts: option,
                                    element: ele,
                                    value: str,
                                    isNullEle: _isNull,
                                    succeedEle: _succeed
                                }, "");
                            } else {
                                callback({
                                    prompts: option,
                                    element: ele,
                                    value: str,
                                    errorEle: _error,
                                    isNullEle: _isNull,
                                    succeedEle: _succeed
                                });
                            }
                        });
                    break;
                default:
                    if (rel && rel == "select") {
                        ele.bind("change", function () {
                            var str = ele.val();
                            callback({
                                prompts: option,
                                element: ele,
                                value: str,
                                errorEle: _error,
                                isNullEle: _isNull,
                                succeedEle: _succeed
                            });
                        })
                    } else {
                        ele.bind("click", function () {
                            callback({
                                prompts: option,
                                element: ele,
                                errorEle: _error,
                                isNullEle: _isNull,
                                succeedEle: _succeed
                            });
                        })
                    }
                    break;
            }
        }
    }
})(jQuery);

//����
var validateSettings = {
    onFocus: {
        state: null,
        container: "_error",
        style: "focus",
        run: function (option, str, expands) {
            if (!validateRules.checkType(option.element)) {
                option.element.removeClass(validateSettings.INPUT_style2).addClass(validateSettings.INPUT_style1);
            }
            option.succeedEle.removeClass(validateSettings.succeed.style);
            option.onFocusEle.removeClass().addClass(validateSettings.onFocus.style).html(str);
            if (expands) {
                expands();
            }
        }
    },
    isNull: {
        state: 0,
        container: "_error",
        style: "null",
        run: function (option, str) {
            option.element.attr("sta", 0);
            if (!validateRules.checkType(option.element)) {
                if (str == "") {
                    option.element.removeClass(validateSettings.INPUT_style2).removeClass(validateSettings.INPUT_style1);
                } else {
                    option.element.removeClass(validateSettings.INPUT_style1).addClass(validateSettings.INPUT_style2);
                }
            }

            option.succeedEle.removeClass(validateSettings.succeed.style);
            if (str == "") {
                option.isNullEle.removeClass().addClass(validateSettings.isNull.style).html(str);
            } else {
                option.isNullEle.removeClass().addClass(validateSettings.error.style).html(str);
            }
        }
    },
    error: {
        state: 1,
        container: "_error",
        style: "error",
        run: function (option, str) {
            option.element.attr("sta", 1);
            if (!validateRules.checkType(option.element)) {
                option.element.removeClass(validateSettings.INPUT_style1).addClass(validateSettings.INPUT_style2);
            }

            option.succeedEle.removeClass(validateSettings.succeed.style);
            option.errorEle.removeClass().addClass(validateSettings.error.style).html(str);
        }
    },
    succeed: {
        state: 2,
        container: "_succeed",
        style: "succeed",
        run: function (option) {
            option.element.attr("sta", 2);
            option.errorEle.empty();
            if (!validateRules.checkType(option.element)) {
                option.element.removeClass(validateSettings.INPUT_style1).removeClass(validateSettings.INPUT_style2);
            }

            option.succeedEle.addClass(validateSettings.succeed.style);
            option.errorEle.removeClass();
        }
    },
    INPUT_style1: "highlight1",
    INPUT_style2: "highlight2"
}

//��֤����
var validateRules = {
    isNull: function (str) {
        return (str == "" || typeof str != "string");
    },
    betweenLength: function (str, _min, _max) {
        return (str.length >= _min && str.length <= _max);
    },
    isUid: function (str) {
        return new RegExp(validateRegExp.username).test(str);
    },
    fullNumberName: function (str) {
        return new RegExp(validateRegExp.fullNumber).test(str);
    },
    isPwd: function (str) {
        return /^.*([\W_a-zA-z0-9-])+.*$/i.test(str);
    },
    isPwdRepeat: function (str1, str2) {
        return (str1 == str2);
    },
    isEmail: function (str) {
        return new RegExp(validateRegExp.email).test(str);
    },
    isTel: function (str) {
        return new RegExp(validateRegExp.tel).test(str);
    },
    isMobile: function (str) {
        return new RegExp(validateRegExp.mobile).test(str);
    },
    checkType: function (element) {
        return (element.attr("type") == "checkbox" || element.attr("type") == "radio" || element.attr("rel") == "select");
    },
    isRealName: function (str) {
        return new RegExp(validateRegExp.realname).test(str);
    },
    isCompanyname: function (str) {
        return new RegExp(validateRegExp.companyname).test(str);
    },
    isCompanyaddr: function (str) {
        return new RegExp(validateRegExp.companyaddr).test(str);
    },
    isCompanysite: function (str) {
        return new RegExp(validateRegExp.companysite).test(str);
    },
    simplePwd: function (str) {
//        var pin = $("#regName").val();
//        if (pin.length > 0) {
//            pin = strTrim(pin);
//            if (pin == str) {
//                return true;
//            }
//        }
        return pwdLevel(str) == 1;
    },
    weakPwd: function (str) {
        for(var i = 0; i < weakPwdArray.length; i++) {
            if(weakPwdArray[i] == str) {
                return true;
            }
        }
        return false;
    }
};
//��֤�ı�
var validatePrompt = {
    regName: {
        onFocus: "����������/�û���/�ֻ���",
        succeed: "",
        isNull: "����������/�û���/�ֻ���",
        error: {
            beUsed: "���û����ѱ�ʹ�ã������������ʹ���Ƽ��û������������&quot;{1}&quot;��������<a href='https://passport.jd.com/uc/login' class='flk13'>��¼</a>",
            badLength: "�û�������ֻ����4-20λ�ַ�֮��",
            badFormat: "�û���ֻ�������ġ�Ӣ�ġ����ּ���_������-�����",
            fullNumberName: "<span>�û��������Ǵ����֣���ȷ����������ֻ��Ż�����������</span>"
        },
        onFocusExpand: function () {
            $("#morePinDiv").removeClass().addClass("intelligent-error hide");
        }
    },

    pwd: {
        onFocus: "<span>6-20λ�ַ�����ʹ����ĸ�����ֻ���ŵ���ϣ�������ʹ�ô����֣�����ĸ��������</span>",
        succeed: "",
        isNull: "����������",
        error: {
            badLength: "���볤��ֻ����6-20λ�ַ�֮��",
            badFormat: "����ֻ����Ӣ�ġ����ּ����������",
            simplePwd: "<span>������Ƚϼ򵥣��б������գ�����������Ϊ�������룬����ĸ+���ֵ����</span>",
            weakPwd: "<span>������Ƚϼ򵥣��б������գ�����������Ϊ��������</span>"
        },
        onFocusExpand: function () {
            $("#pwdstrength").hide();
        }
    },
    pwdRepeat: {
        onFocus: "���ٴ���������",
        succeed: "",
        isNull: "����������",
        error: {
            badLength: "���볤��ֻ����6-20λ�ַ�֮��",
            badFormat2: "�����������벻һ��",
            badFormat1: "����ֻ����Ӣ�ġ����ּ����������"
        }
    },
    mobileCode: {
        onFocus: "",
        succeed: "",
        isNull: "�����������֤��",
        error: "��֤�����"
    },
    protocol: {
        onFocus: "",
        succeed: "",
        isNull: "�����Ķ���ͬ�⡶�����û�ע��Э�顷",
        error: ""
    },
    empty: {
        onFocus: "",
        succeed: "",
        isNull: "",
        error: ""
    }
};

var nameold, morePinOld, emailResult;
var namestate = false;
//�ص�����
var validateFunction = {
    regName: function (option) {
        $("#intelligent-regName").empty().hide();
        var regName = option.value;
        if (validateRules.isNull(regName) || regName == '����/�û���/�ֻ���') {
            option.element.removeClass(validateSettings.INPUT_style2).removeClass(validateSettings.INPUT_style1);
            $("#regName_error").removeClass().empty();
            return;
        }

        if (regName.indexOf("@") > -1) {
            $("#mobileCodeDiv").removeClass().addClass("item hide");
            $("#authcodeDiv").show();
            checkEmail(option);
            return;
        }
        if (validateRules.isMobile(regName)) {
            checkMobile(option);
            return;
        }
        $("#mobileCodeDiv").removeClass().addClass("item hide");
        $("#authcodeDiv").show();
        checkPin(option);
    },

    pwd: function (option) {
        var str1 = option.value;
        var regName = $("#regName").val();
        if ((validateRules.isNull(regName) == false) && (regName != '����/�û���/�ֻ���') && regName == str1) {
            $("#pwdstrength").hide();
            validateSettings.error.run(option, "<span>�����������˻���Ϣ̫�غϣ��б������գ��뻻һ������</span>");
            return;
        }

        var str2 = $("#pwdRepeat").val();
        var format = validateRules.isPwd(option.value);
        var length = validateRules.betweenLength(option.value, 6, 20);

        $("#pwdstrength").hide();
        if (!length && format) {
            validateSettings.error.run(option, option.prompts.error.badLength);
        } else if (!length && !format) {
            validateSettings.error.run(option, option.prompts.error.badFormat);
        } else if (length && !format) {
            validateSettings.error.run(option, option.prompts.error.badFormat);
        } else if (validateRules.weakPwd(str1)) {
            validateSettings.error.run(option, option.prompts.error.weakPwd);
        } else {

            validateSettings.succeed.run(option);
            validateFunction.pwdstrength();
            if (validateRules.simplePwd(str1)) {
                $("#pwd_error").removeClass().addClass("focus");
                $("#pwd_error").empty().html(option.prompts.error.simplePwd);
                return;
            }
        }
        if (str2 == str1) {
            $("#pwdRepeat").focus();
        }
    },
    pwdRepeat: function (option) {
        var str1 = option.value;
        var str2 = $("#pwd").val();
        var length = validateRules.betweenLength(option.value, 6, 20);
        var format2 = validateRules.isPwdRepeat(str1, str2);
        var format1 = validateRules.isPwd(str1);
        if (!length) {
            validateSettings.error.run(option, option.prompts.error.badLength);
        } else {
            if (!format1) {
                validateSettings.error.run(option, option.prompts.error.badFormat1);
            } else {
                if (!format2) {
                    validateSettings.error.run(option, option.prompts.error.badFormat2);
                }
                else {
                    validateSettings.succeed.run(option);
                }
            }
        }
    },

    mobileCode: function (option) {
        var bool = validateRules.isNull(option.value);
        if (bool) {
            validateSettings.error.run(option, option.prompts.error);
            return;
        } else {
            validateSettings.succeed.run(option);
        }
    },
    protocol: function (option) {
        if (option.element.attr("checked") == true) {
            option.element.attr("sta", validateSettings.succeed.state);
            option.errorEle.html("");
        } else {
            option.element.attr("sta", validateSettings.isNull.state);
            option.succeedEle.removeClass(validateSettings.succeed.style);
        }
    },
    pwdstrength: function () {
        var element = $("#pwdstrength");
        var value = $("#pwd").val();
        if (value.length >= 6 && validateRules.isPwd(value)) {
            $("#pwd_error").removeClass('focus');
            $("#pwd_error").empty();
            element.show();
            var level = pwdLevel(value);
            switch (level) {
                case 1:
                    element.removeClass().addClass("strengthA");
                    break;
                case 2:
                    element.removeClass().addClass("strengthB");
                    break;
                case 3:
                    element.removeClass().addClass("strengthC");
                    break;
                default:
                    break;
            }
        } else {
            element.hide();
        }
    },
    checkGroup: function (elements) {
        for (var i = 0; i < elements.length; i++) {
            if (elements[i].checked) {
                return true;
            }
        }
        return false;
    },
    checkSelectGroup: function (elements) {
        for (var i = 0; i < elements.length; i++) {
            if (elements[i].value == -1) {
                return false;
            }
        }
        return true;
    },

    FORM_submit: function (elements) {
        var bool = true;
        for (var i = 0; i < elements.length; i++) {
            if ($(elements[i]).attr("sta") == 2) {
                bool = true;
            } else {
                bool = false;
                break;
            }
        }

        return bool;
    }
};

var checkpin = -10;
function checkPin(option) {
    var pin = option.value;
    if (!validateRules.betweenLength(pin.replace(/[^\x00-\xff]/g, "**"), 4, 20)) {
        validateSettings.error.run(option, option.prompts.error.badLength);
        return false;
    }

    if (!validateRules.isUid(pin)) {
        validateSettings.error.run(option, option.prompts.error.badFormat);
        return;
    }
    if (validateRules.fullNumberName(pin)) {
        validateSettings.error.run(option, option.prompts.error.fullNumberName);
        return;
    }
    if (!namestate || nameold != pin) {
        if (nameold != pin) {
            nameold = pin;
            option.errorEle.html("<em style='color:#999'>�����С���</em>");
            $.getJSON("../validate/isPinEngaged?pin=" + escape(pin) + "&r=" + Math.random(), function (date) {
                checkpin = date.success;
                if (date.success == 0) {
                    validateSettings.succeed.run(option);
                    namestate = true;
                } else if (date.success == 2) {
                    validateSettings.error.run(option, "�û��������˷Ƿ���");
                    namestate = false;
                } else {
                    validateSettings.error.run(option, "<span>" + option.prompts.error.beUsed.replace("{1}", option.value) + "</span>");
                    namestate = false;
                    morePinOld = date.morePin;
                    if (date.morePin != null && date.morePin.length > 0) {
                        var html = ""
                        for (var i = 0; i < date.morePin.length; i++) {
                            html += "<div class='item-fore'><input name='morePinRadio' onclick='selectMe(this);' type='radio' class='radio' value='" + date.morePin[i] + "'/><label>" + date.morePin[i] + "</label></div>"
                        }
                        $("#morePinGroom").empty();
                        $("#morePinGroom").html(html);
                        $("#morePinDiv").removeClass().addClass("intelligent-error");
                    }
                }
            });
        } else {

            if (checkpin == 2) {
                validateSettings.error.run(option, "�û��������˷Ƿ���");
            } else {
                validateSettings.error.run(option, "<span>" + option.prompts.error.beUsed.replace("{1}", option.value) + "</span>");
                if (morePinOld != null && morePinOld.length > 0) {
                    $("#morePinDiv").removeClass().addClass("intelligent-error");
                }
            }
            namestate = false;
        }
    } else {
        validateSettings.succeed.run(option);
    }
}

function selectMe(option) {
    $("#morePinDiv").removeClass().addClass("intelligent-error hide");
    $("#regName").val(option.value);
    $("#regName").blur();
}

function checkEmail(option) {
    var email = option.value;
    var email = strTrim(option.value);
    var format = validateRules.isEmail(email);
    var format2 = validateRules.betweenLength(email, 0, 50);
    if (!format) {
        validateSettings.error.run(option, "�����ַ����ȷ������������");
    } else {
        if (!format2) {
            validateSettings.error.run(option, "�����ַ����Ӧ��4-50���ַ�֮��");
        } else {
            if (!namestate || nameold != email) {
                if (nameold != email) {
                    nameold = email;
                    option.errorEle.html("<em style='color:#999'>�����С���</em>");
                    $.getJSON("../validate/isEmailEngaged?email=" + escape(option.value) + "&r=" + Math.random(), function (date) {

                        emailResult = date.success;
                        if (date.success == 0) {
                            validateSettings.succeed.run(option);
                            namestate = true;
                            if ($("#mail")) {
                                $("#mail").val(option.value);
                            }
                        }
                        if (date.success == 1) {
                            validateSettings.error.run(option, "�������Ѵ��ڣ�����<a  class='flk13' href='https://passport.jd.com/uc/login'>��¼</a>");
                            namestate = false;
                        }
                        if (date.success == 2) {
                            validateSettings.error.run(option, "�����ַ����ȷ������������");
                            namestate = false;
                        }
                        if (date.success == 3) {
                            validateSettings.error.run(option, "<span>�й��Ż������Ѿ�ֹͣ����,������һ������</span>");
                            namestate = false;
                        }
                    })
                }
                else {
                    namestate = false;
                    if (emailResult == 1) {
                        validateSettings.error.run(option, "�������Ѵ��ڣ�����<a  class='flk13' href='https://passport.jd.com/uc/login'>��¼</a>");
                    }
                    if (emailResult == 2) {
                        validateSettings.error.run(option, "�����ַ����ȷ������������");

                    }
                    if (emailResult == 3) {
                        validateSettings.error.run(option, "<span>�й��Ż������Ѿ�ֹͣ����,������һ������</span>");
                    }
                }
            }
            else {
                validateSettings.succeed.run(option);
            }
        }
    }
}
function checkMobile(option) {
    var mobileValue = option.value;
    mobileValue = strTrim(mobileValue);
    var isMobile = validateRules.isMobile(mobileValue);
    if (!isMobile || mobileValue.length > 11) {
        validateSettings.error.run(option, option.prompts.error.badFormat);
    } else {
        if (!namestate || nameold != option.value) {
            if (nameold != option.value) {
                nameold = option.value;
                option.errorEle.html("<em style='color:#999'>�����С���</em>");
                $.getJSON("../validate/isMobileEngaged?mobile=" + option.value + "&r=" + Math.random(), function (date) {
                    if (date.success == 0) {
                        validateSettings.succeed.run(option);
                        $("#mobileCodeDiv").removeClass().addClass("item");
                        $("#authcodeDiv").hide();
                        namestate = true;

                        if ($("#mobile")) {
                            $("#mobile").val(option.value);
                        }
                    } else {
                        validateSettings.error.run(option, "���ֻ����Ѵ��ڣ�����<a  class='flk13' href='https://passport.jd.com/uc/login'>��¼</a>");
                        namestate = false;
                    }
                })
            } else {
                validateSettings.error.run(option, "���ֻ����Ѵ��ڣ�����<a  class='flk13' href='https://passport.jd.com/uc/login'>��¼</a>");
                namestate = false;
            }
        } else {
            validateSettings.succeed.run(option);
        }
    }
}

function sendMobileCode() {
    var mobile = $("#regName").val();
    if (validateRules.isNull(mobile) || !validateRules.isMobile(mobile)) {
        $("#regName_error").html("<span>�ֻ������ʽ������������13/14/15/18��ͷ��11λ���֡�<span>");
        $("#regName_error").removeClass().addClass("error");
        //  $("#regName").removeClass().addClass("text highlight2");
        $("#regName_error").show();
        return;
    }
    if ($("#sendMobileCode").attr("disabled")) {
        return;
    }
    $("#sendMobileCode").attr("disabled", "disabled");

    jQuery.ajax({
        type: "get",
        url: "../notify/mobileCode?mobile=" + $("#regName").val() + "&r=" + Math.random(),
        success: function (result) {
            if (result) {
                var obj = eval(result);
                if (obj.rs == 1 || obj.remain) {
                    $("#mobileCode_error").addClass("hide");
                    $("#dyMobileButton").html("120������»�ȡ");
                    if (obj.remain) {
                        $("#mobileCodeSucMessage").empty().html(obj.remain);
                    } else {
                        $("#mobileCodeSucMessage").empty().html("��֤���ѷ��ͣ�����ն��š�");
                    }

                    setTimeout(countDown, 1000);
                    $("#sendMobileCode").removeClass().addClass("btn btn-15").attr("disabled", "disabled");
                    $("#mobileCode").removeAttr("disabled");
                }
                if (obj.rs == -1) {
                    $("#regName_error").html("<span>�ֻ������ʽ������������13/14/15/18��ͷ��11λ���֡�</span>");
                    $("#regName_error").removeClass().addClass("error");
                    $("#regName").removeClass().addClass("text highlight2");
                    $("#sendMobileCode").removeClass().addClass("btn").removeAttr("disabled");
                }
                if (obj.info) {
                    mobileCodeError(obj.info);
                }

                if (obj.rs == -2) {
                    mobileCodeError("���緱æ�����Ժ����»�ȡ��֤��");
                }
            }
        }
    });
}

function mobileCodeError(content) {
    $("#mobileCode_error").html(content);
    $("#mobileCode_error").removeClass().addClass("error");
    $("#mobileCode_error").show();
    $("#sendMobileCode").removeClass().addClass("btn").removeAttr("disabled");
}
var delayTime = 120;
function countDown() {
    delayTime--;
    $("#dyMobileButton").html(delayTime + '������»�ȡ');
    if (delayTime == 0) {
        delayTime = 120;
        $("#mobileCodeSucMessage").empty();
        $("#dyMobileButton").html("��ȡ������֤��");
        $("#mobileCode_error").addClass("hide");
        $("#sendMobileCode").removeClass().addClass("btn").removeAttr("disabled");
    } else {
        setTimeout(countDown, 1000);
    }
}

function strTrim(str) {
    return str.replace(/(^\s*)|(\s*$)/g, "");
}
var emailSurfixArray = ['@163.com', '@126.com', '@qq.com', '@sina.com', '@gmail.com', '@sohu.com', '@vip.163.com', '@vip.126.com', '@188.com', '@139.com', '@yeah.net'];

function moreName(event) {
    var sval = this.value;
    event = event ? event : window.event;
    var keyCode = event.keyCode;
    var vschool = $('#intelligent-regName');
    if (keyCode == 40 || keyCode == 38 || keyCode == 13) {
        var tipindex = $("#hnseli").val() == "" ? -1 : $("#hnseli").val();
        var fobj;
        if (keyCode == 40) {
            tipindex++;
            if (tipindex == vschool.find("li").length) {
                tipindex = 0;
                vschool.find("li").eq(vschool.find("li").length - 1).css("background-color", "");
            }
            fobj = vschool.find("li").eq(tipindex);
            vschool.find("li").eq(tipindex - 1).css("background-color", "");
            fobj.css("background-color", "#EEEEEE");
            $("#regName").val(fobj.html().replace(/<(\S*?)[^>]*>|<.*? \/>/g, ""));
            $("#schoolid").val(fobj.attr("value"));
            $("#hnseli").val(tipindex);
            return;
        } else if (keyCode == 38) {
            tipindex--;
            if (tipindex <= -1) {
                tipindex = vschool.find("li").length - 1;
                vschool.find("li").eq(0).css("background-color", "");
            }
            vschool.find("li").eq(tipindex + 1).css("background-color", "");
            fobj = vschool.find("li").eq(tipindex);
            fobj.css("background-color", "#EEEEEE");
            if (fobj.html() != null) {
                $("#regName").val(fobj.html().replace(/<(\S*?)[^>]*>|<.*? \/>/g, ""));
                $("#schoolid").val(fobj.attr("value"));
            }
            $("#hnseli").val(tipindex);
            return;
        } else if (keyCode == 13) {
            $("#hnseli").val("-1");
            if ($("#regName").val().length >= 1) {
                var combinedValue = vschool.find("li").eq(tipindex).html();
                if (combinedValue != null) {
                    $("#regName").val(combinedValue.replace(/<(\S*?)[^>]*>|<.*? \/>/g, ""));
                }
                vschool.empty().hide();
                if ($("#schoolid").val() != "") {
                    $("#hnschool").val("1");
                    $("#hnschool").attr("sta", 2);
                    $("#regName").blur();
                } else {
                    $("#hnschool").val("-1");
                    $("#hnschool").attr("sta", 0);
                    $("#regNamel_error").html("");
                    $("#regName_succeed").removeClass("succeed");
                }
                return;
            }
        }
    } else {
        //hide morePin
        $("#morePinDiv").removeClass().addClass("intelligent-error hide");

        if (sval != "") {
            var userinput = sval;
            var oldSval = "";
            var pos = sval.indexOf("@");
            if (pos >= 0) {
                oldSval = sval.substring(0, pos);
            }

            $("#schoolid").val("");
            $("#hnseli").val("-1");
            var html = "";
            if (/[\u4E00-\u9FA5]/g.test(sval) || sval.indexOf("-") > -1 || sval.indexOf("_") > -1) {
                html = "<li>" + sval + "</li>";
            } else {
                if (oldSval != '') {
                    sval = oldSval;
                }
                if (userinput.indexOf("@") == 0) {
                    sval = "";
                }
                html = "<li>" + userinput + "</li>";
                var partSurfix = initEmailSurfixArray(userinput);
                if (partSurfix != null) {
                    for (var i = 0; i < partSurfix.length; i++) {
                        html += "<li>" + sval + partSurfix[i] + "</li>";
                    }
                }
            }
            if (sval.length > 25) {
                $('#intelligent-regName').hide();
            } else {
                $('#intelligent-regName').show();
                $('#intelligent-regName').html(html).find("li").mousedown(function () {
                    $("#regName").val($(this).html());
                    $("#schoolid").val($(this).attr("value"));
                    $("#hnseli").val("-1");
                });
            }
        } else {
            $('#intelligent-regName').html("").hide();
            $("#schoolid").val("");
            $("#hnseli").val("-1");
        }
    }
}

$("#regName").keyup(moreName);
$("#regName").focus(moreName);

function initEmailSurfixArray(str) {
    var pos = str.indexOf("@");
    if (pos < 0 || pos == (str.length - 1)) {
        return emailSurfixArray;
    }
    var inputSurfix = str.substring(pos, str.length);
    var suitableSurfixArray = [];
    var j = 0;
    for (var i = 0; i < emailSurfixArray.length; i++) {
        if (emailSurfixArray[i].indexOf(inputSurfix) == 0) {
            suitableSurfixArray[j] = emailSurfixArray[i];
            j++;
        }
    }

    return suitableSurfixArray;
}

$("#intelligent-regName li").livequery("mouseover",function () {
    var vi = $(this).attr("dex");
    var tipindex = $("#hnseli").val() == "" ? -1 : $("#hnseli").val();
    if (tipindex <= 0) {
        tipindex = 0;
    }
    $('#intelligent-regName').find("li").eq(tipindex).css("background-color", "");
    $(this).css("background-color", "#EEEEEE");
    $("#hnseli").val($(this).attr("dex"));
}).livequery("mouseleave", function () {
        var tipindex = $("#hnseli").val() == "" ? -1 : $("#hnseli").val();
        if (tipindex <= 0) {
            tipindex = 0;
        }
        $(this).css("background-color", "");
        $("#hnseli").val("-1");
    });

$("#regName").blur(function () {
    setTimeout(function () {
        if ($("#schoolid").val() == "") {
            $("#schoolinput").val("");
            $("#hnschool").val("-1");
            $("#hnschool").attr("sta", 0);
            $("#schoolinput_succeed").removeClass("succeed");
        } else {
            $("#hnschool").val("1");
            $("#hnschool").attr("sta", 2);
            $("#schoolinput_error").html("");
            $("#schoolinput_succeed").addClass("succeed");
        }
        $('#intelligent-school').hide().empty();
        $("#hnseli").val("-1");
    }, 200)
})

// �û�Э��
$(function () {
    $('#protocol').click(function () {
        jQuery.jdThickBox({
            type: "text",
            title: "�����û�ע��Э��",
            width: 922,
            height: 450,
            source: "<div class=\" regist-2013\">" +
                "<div class=\"regist-bor\">" +
                "<div class=\"mc\">" +
                "<div id=\"protocol-con\">" +
                " <h4>�����û�ע��Э��</h4>" +

                "    <p>" +
                "        ��Э�������뾩����վ�����\"��վ\"����ַ��www.jd.com�������ߣ����¼��Ϊ\"����\"��֮��;�����վ����������������������Լ��������ϸ�Ķ���ע��Э�飬�����\"ͬ�Ⲣ����\"��ť�󣬱�Э�鼴���ɶ�˫����Լ�����ķ����ļ���</p>" +
                "    <h5> ��1�� ��վ���������ȷ�Ϻͽ���</h5>" +

                "    <p>" +
                "        <strong>1.1</strong>��վ�ĸ�����ӷ��������Ȩ������Ȩ�龩�����С��û�ͬ������ע��Э��������ע����򣬲��ܳ�Ϊ��վ����ʽ�û����û�ȷ�ϣ���Э�������Ǵ���˫��Ȩ���������Լ��ʼ����Ч����������ǿ���Թ涨��˫�������ر�Լ���ģ�����涨��" +
                "    </p>" +

                "    <p>" +
                "        <strong>1.2</strong>�û����ͬ�ⱾЭ��ģ�����Ϊ�û�ȷ���Լ��������ܱ�վ�����µ��������Ӧ��Ȩ����������Ϊ�������ܹ������е��������Ρ�</p>" +

                "    <p>" +
                "        <strong>1.3</strong>�������18�������£���ֻ���ڸ�ĸ��໤�˵ļ໤�����²���ʹ�ñ�վ��</p>" +

                "    <p>" +
                "        <strong>1.4</strong>�����������л����񹲺͹���½������ʩ��֮��������ķ�Χ�ڶ��Ծ����ܾ����񡢹ر��û��˻��������༭���ݻ�ȡ��������Ȩ����</p>" +
                "    <h5> ��2�� ��վ����</h5>" +

                "    <p>" +
                "        <strong>2.1</strong>����ͨ������������Ϊ�û��ṩ��������Ϣ�ȷ����û�����ȫͬ�ⱾЭ�鼰��վ�涨������£�����Ȩʹ�ñ�վ����ط���</p>" +

                "    <p>" +
                "        <strong>2.2</strong>�û���������׼�������豸�ͳе����¿�֧����1�������豸�������������ڵ��Ի������������նˡ����ƽ�����������ر�������װ�ã���2��������֧���������������������ѡ������豸���÷ѡ��ֻ������ѵȡ�" +
                "    </p>" +
                "    <h5> ��3�� �û���Ϣ</h5>" +

                "    <p>" +
                "        <strong>3.1</strong>�û�Ӧ���г�����վ�ṩע�����ϣ��û�ͬ�����ṩ��ע��������ʵ��׼ȷ���������Ϸ���Ч���û�ע���������б䶯�ģ�Ӧ��ʱ������ע�����ϡ�����û��ṩ��ע�����ϲ��Ϸ�������ʵ����׼ȷ�����꾡�ģ��û���е�����������Ӧ���μ���������Ҿ���������ֹ�û�ʹ�þ�����������Ȩ����" +
                "    </p>" +

                "    <p>" +
                "        <strong>3.2</strong>�û��ڱ�վ����������µ�����Ȼʱ���漰�û���ʵ����/���ơ�ͨ�ŵ�ַ����ϵ�绰�������������˽��Ϣ�ģ���վ�������ϸ��ܣ����ǵõ��û�����Ȩ�������й涨����վ�����������¶�û���˽��Ϣ��" +
                "    </p>" +

                "    <p>" +
                "        <strong>3.3</strong>�û�ע��ɹ��󣬽������û�����������˻���Ϣ�������Ը��ݱ�վ�涨�ı��������롣�û�Ӧ��������ı��桢ʹ�����û��������롣�û��������κηǷ�ʹ���û��˺Ż���ڰ�ȫ©���������������֪ͨ��վ���򹫰����ر�����" +
                "    </p>" +

                "    <p>" +
                "        <strong>3.4</strong><strong>�û�ͬ�⣬����ӵ��ͨ���ʼ������ŵ绰����ʽ�����ڱ�վע�ᡢ�����û����ջ��˷��Ͷ�����Ϣ��������ȸ�֪��Ϣ��Ȩ����</strong></p>" +

                "    <p>" +
                "        <strong>3.5</strong><strong>�û����ý��ڱ�վע���õ��˻��������ʹ�ã������û�Ӧ�е��ɴ˲�����ȫ�����Σ�����ʵ��ʹ���˳е��������Ρ�</strong></p>" +

                "    <p>" +
                "        <strong>3.6</strong><strong>�û�ͬ�⣬������Ȩʹ���û���ע����Ϣ���û������������Ϣ����½�����û���ע���˻�������֤�ݱ�ȫ�������������ڹ�֤����֤�ȡ�</strong></p>" +
                "    <h5> ��4�� �û�������������</h5>" +

                "    <p> ��Э�����ݹ�����ط��ɷ�������ƶ����û�ͬ���ϸ�������������</p>" +

                "    <p>" +
                "        <strong>��1��</strong>���ô���򷢱�ɿ�����ܡ��ƻ��ܷ��ͷ��ɡ���������ʵʩ�����ۣ�ɿ���߸�������Ȩ���Ʒ���������ƶȵ����ۣ�ɿ�����ѹ��ҡ��ƻ�����ͳһ�ĵ����ۣ�ɿ�������ޡ��������ӡ��ƻ������Ž�����ۣ�" +
                "    </p>" +

                "    <p>" +
                "        <strong>��2��</strong>���й���½���⴫��������Ϣʱ��������й��йط��棻</p>" +

                "    <p>" +
                "        <strong>��3��</strong>�������ñ�վ����ϴǮ����ȡ��ҵ���ܡ���ȡ������Ϣ��Υ��������" +
                "    </p>" +

                "    <p>" +
                "        <strong>��4��</strong>���ø��ű�վ��������ת���������뱾վ�����Ҽ������Ϣϵͳ��</p>" +

                "    <p>" +
                "        <strong>��5��</strong>���ô���򷢱��κ�Υ������ġ�ɧ���Եġ��������˵ġ������Եġ������Եġ��˺��Եġ�ӹ�׵ģ�����ġ��������ĵ���Ϣ���ϣ�</p>" +

                "    <p>" +
                "        <strong>��6��</strong>���ô���򷢱��𺦹�����ṫ��������漰���Ұ�ȫ����Ϣ���ϻ����ۣ�</p>" +

                "    <p>" +
                "        <strong>��7��</strong>���ý������˴��±�������ֹ����Ϊ��</p>" +

                "    <p>" +
                "        <strong>��8��</strong>���������ڱ�վע����˻�����Ĳ���Ծ�Ӫ���</p>" +

                "    <p>" +
                "        <strong>��9��</strong>���÷����κ��ַ���������Ȩ���̱�Ȩ��֪ʶ��Ȩ��Ϸ�Ȩ�������ݣ�</p>" +

                "    <p>" +
                "        �û�Ӧ��ʱ��ע�����ر�վ��ʱ�������޸ĵĸ���Ϸ�����涨��</p>" +

                "    <p>" +
                "        <strong>��վ����ɾ��վ�ڸ��಻���Ϸ������߻���ʵ����Ϣ���ݶ�����֪ͨ�û���Ȩ����</strong></p>" +

                "    <p>" +
                "        <strong>���û�δ�������Ϲ涨�ģ���վ��Ȩ���������жϲ���ȡ��ͣ��ر��û��ʺŵȴ�ʩ��</strong>�û�����Լ������ϵ����ۺ���Ϊ�е��������Ρ�</p>" +
                "    <h5> ��5�� ��Ʒ��Ϣ</h5>" +

                "    <p>" +
                "        ��վ�ϵ���Ʒ�۸��������Ƿ��л�����Ʒ��Ϣ��ʱ���п��ܷ����䶯����վ�����ر�֪ͨ��������վ����Ʒ��Ϣ�����������Ӵ���Ȼ��վ�ᾡ���Ŭ����֤���������Ʒ��Ϣ��׼ȷ�ԣ�������������֪�Ļ������������صȿ͹�ԭ����ڣ���վ��ҳ��ʾ����Ϣ���ܻ���һ�����ͺ��Ի����Դ�������֪Ϥ����⣻������ӭ����������������������һ���Ľ�����</p>" +

                "    <p> Ϊ������������Ʒ�ͷ�����Ϊ\"��Ʒ\"��\"����\"��</p>" +
                "    <h5> ��6�� ����</h5>" +

                "    <p>" +
                "        <strong>6.1</strong>�����¶���ʱ��������ϸȷ��������Ʒ�����ơ��۸��������ͺš���񡢳ߴ硢��ϵ��ַ���绰���ջ��˵���Ϣ��<span>�ջ������û����˲�һ�µģ��ջ��˵���Ϊ����˼��ʾ��Ϊ�û�����Ϊ����˼��ʾ���û�Ӧ���ջ��˵���Ϊ����˼��ʾ�ķ��ɺ���е��������Ρ�</span>" +
                "    </p>" +

                "    <p>" +
                "        <strong>6.2</strong><strong>����������ǿ���Թ涨�⣬˫��Լ�����£���վ�����۷�չʾ����Ʒ�ͼ۸����Ϣ������ҪԼ���룬���µ�ʱ����д��ϣ���������Ʒ�������ۿ֧����ʽ���ջ��ˡ���ϵ��ʽ���ջ���ַ����ͬ���еص㣩����ͬ���з�ʽ�����ݣ�ϵͳ���ɵĶ�����Ϣ�Ǽ������Ϣϵͳ��������д�������Զ����ɵ����ݣ������������۷������ĺ�ͬҪԼ�����۷��յ����Ķ�����Ϣ��ֻ�������۷������ڶ����ж�������Ʒ�Ӳֿ�ʵ��ֱ����������ʱ��" +
                "        ����Ʒ����Ϊ��־��������Ϊ�������۷�֮���ʵ��ֱ��������������Ʒ�����˺�ͬ��ϵ���������һ�ݶ����ﶩ���˶�����Ʒ�������۷�ֻ���������˲�����Ʒʱ���������۷�֮�����ʵ��ֱ��������������Ʒ�����˺�ͬ��ϵ��ֻ�������۷�ʵ��ֱ�����������˶����ж�����������Ʒʱ���������۷�֮��Ͷ����и�������ʵ��ֱ��������������Ʒ�ų�����ͬ��ϵ����������ʱ��½���ڱ�վע����˻�����ѯ���Ķ���״̬��</strong>" +
                "    </p>" +

                "    <p>" +
                "        <strong>6.3</strong><strong>�����г��仯�������Ժ�����ҵŬ�����Կ��Ƶ����ص�Ӱ�죬��վ�޷���֤���ύ�Ķ�����Ϣ��ϣ���������Ʒ�����л��������⹺�����Ʒ������ȱ��������Ȩȡ��������</strong>" +
                "    </p>" +
                "    <h5> ��7�� ����</h5>" +

                "    <p>" +
                "        <strong>7.1</strong>���۷��������Ʒ������͵�����ָ�����ջ���ַ�������ڱ�վ���г����ͻ�ʱ��Ϊ�ο�ʱ�䣬�ο�ʱ��ļ����Ǹ��ݿ��״���������Ĵ�����̺��ͻ�ʱ�䡢�ͻ��ص�Ļ����Ϲ��Ƶó��ġ�</p>" +
                "" +
                "    <p>" +
                "        <strong>7.2</strong>�����������ɶ����ӳٻ��޷����͵ȣ����۷����е��ӳ����͵����Σ�</p>" +

                "    <p>" +
                "        <strong>��1��</strong>�û��ṩ����Ϣ���󡢵�ַ����ϸ��ԭ���µģ�" +
                "    </p>" +

                "    <p>" +
                "        <strong>��2��</strong>�����ʹ������ǩ�գ������޷����ͻ��ӳ����͵ģ�</p>" +

                "    <p>" +
                "        <strong>��3��</strong>���Ʊ�����ص��µģ�</p>" +

                "    <p>" +
                "        <strong>��4��</strong>���ɿ������ص��µģ����磺��Ȼ�ֺ�����ͨ���ϡ�ͻ��ս���ȡ�</p>" +
                "    <h5> ��8�� ����Ȩ��֪ʶ��Ȩ����</h5>" +

                "    <p>" +
                "        <strong>8.1</strong><strong>�û�һ�����ܱ�Э�飬���������û������������κ�ʱ����ڱ�վ������κ���ʽ����Ϣ���ݣ������������ڿͻ����ۡ��ͻ���ѯ�����໰�����µ���Ϣ���ݣ��ĲƲ���Ȩ�����κο�ת�õ�Ȩ����������Ȩ�Ʋ�Ȩ�������������ڣ�����Ȩ������Ȩ������Ȩ��չ��Ȩ������Ȩ����ӳȨ���㲥Ȩ����Ϣ���紫��Ȩ������Ȩ���ı�Ȩ������Ȩ�����Ȩ�Լ�Ӧ��������Ȩ�����е�������ת��Ȩ������ȫ�������Ҳ��ɳ�����ת�ø��������У��û�ͬ�⾩����Ȩ���κ�������Ȩ�������������ϡ�</strong>" +
                "    </p>" +

                "    <p>" +
                "        <strong>8.2</strong><strong>��Э���Ѿ����ɡ��л����񹲺͹�����Ȩ�����ڶ�ʮ�����������������2011�������Ȩ��ȷ��������ط��ɹ涨�������Ʋ�Ȩ��Ȩ��ת������Э�飬��Ч�������û��ھ�����վ�Ϸ������κ�������Ȩ����������Ʒ���ݣ����۸õ������γ��ڱ�Э�鶩��ǰ���Ǳ�Э�鶩����</strong>" +
                "    </p>" +

                "    <p>" +
                "        <strong>8.3</strong><strong>�û�ͬ�Ⲣ�ѳ���˽ⱾЭ��������ŵ�����ѷ����ڱ�վ����Ϣ�����κ���ʽ��������Ȩ�����������κη�ʽʹ�ã������������ڸ�����վ��ý����ʹ�ã���</strong></p>" +

                "    <p>" +
                "        <strong>8.4</strong><strong>�����Ǳ�վ��������,ӵ�д���վ���ݼ���Դ������Ȩ�ȺϷ�Ȩ��,�ܹ��ҷ��ɱ���,��Ȩ��ʱ�ضԱ�Э�鼰��վ�����ݽ����޸ģ����ڱ�վ��������������֪ͨ�û����ڷ������������޶ȷ�Χ�ڣ������Ա�Э�鼰��վ����ӵ�н���Ȩ��</strong>" +
                "    </p>" +

                "    <p>" +
                "        <strong>8.5</strong><strong>����������ǿ���Թ涨�⣬δ��������ȷ���ر��������,�κε�λ����˲������κη�ʽ�Ƿ���ȫ���򲿷ָ��ơ�ת�ء����á����ӡ�ץȡ����������ʽʹ�ñ�վ����Ϣ���ݣ����򣬾�����Ȩ׷���䷨�����Ρ�</strong>" +
                "    </p>" +
                "    <p>" +
                "        <strong>8.6</strong>��վ�����ǵ�������Ϣ���������֡�ͼ����ʶ����ťͼ�ꡢͼ�������ļ�Ƭ�Ρ��������ء����ݱ༭������������Ǿ������������ṩ�ߵĲƲ������й��͹��ʰ�Ȩ���ı�������վ���������ݵĻ���Ǿ����������Ʋ������й��͹��ʰ�Ȩ���ı�������վ������������Ǿ������������˾���������Ӧ�̵ĲƲ������й��͹��ʰ�Ȩ���ı�����" +
                "    </p>" +
                "    <h5> ��9�� �������Ƽ�����ŵ����</h5>" +
                "    <p>" +
                "        <strong>����������ȷ������˵��,��վ�����������Ļ���������ʽͨ����վ�ṩ������ȫ����Ϣ�����ݡ����ϡ���Ʒ������������ͷ��񣬾�����\"����״\"��\"������\"�Ļ������ṩ�ġ�</strong></p>" +

                "    <p>" +
                "        <strong>����������ȷ������˵��,�������Ա�վ����Ӫ��������ڱ���վ�ϵ���Ϣ�����ݡ����ϡ���Ʒ�������������������κ���ʽ�ġ���ʾ��Ĭʾ�������򵣱��������л����񹲺͹��������й涨�����⣩��</strong>" +
                "    </p>" +
                "    <p>" +
                "        <strong>������������վ�������Ļ���������ʽͨ����վ�ṩ������ȫ����Ϣ�����ݡ����ϡ���Ʒ������������ͷ������������ӱ�վ�����ĵ����ż�����Ϣû�в����������к��ɷ֡�</strong></p>" +
                "    <p>" +
                "        <strong>���򲻿ɿ�����������վ�޷����Ƶ�ԭ��ʹ��վ����ϵͳ�������޷�����ʹ�õ������Ͻ����޷���ɻ�ʧ�йص���Ϣ����¼�ȣ����������ؾ���Э�������ƺ����ˡ�</strong></p>" +
                "    <h5> ��10�� Э����¼��û���ע����</h5>" +
                "    ���ݹ��ҷ��ɷ���仯����վ��Ӫ��Ҫ��������Ȩ�Ա�Э�����ʱ�ؽ����޸ģ��޸ĺ��Э��һ���������ڱ�վ�ϼ���Ч��������ԭ����Э�顣�û�����ʱ��½��������Э�飻<strong><em>�û�������ʱ��ע���Ķ����°��Э�鼰��վ���档���û���ͬ����º��Э�飬������Ӧ����ֹͣ���ܾ�����վ���ݱ�Э���ṩ�ķ������û�����ʹ�ñ���վ�ṩ�ķ���ģ�����Ϊͬ����º��Э�顣������������ʹ�ñ�վ֮ǰ�Ķ���Э�鼰��վ�Ĺ��档</em></strong>" +
                "    �����Э�����κ�һ������Ϊ��ֹ����Ч�����κ����ɲ���ִ�У�����Ӧ��Ϊ�ɷֵ��Ҳ���Ӱ���κ������������Ч�ԺͿ�ִ���ԡ�" +
                "    <h5> ��11�� ���ɹ�Ͻ������</h5>" +
                "    ��Э��Ķ�����ִ�кͽ��ͼ�����Ľ����Ӧ�������л����񹲺͹���½��������֮��Ч���ɣ������������ͻ�����򣩡� �緢����Э��������֮������ִ�ʱ������Щ�����ȫ�����ɹ涨���½��ͣ���������Ч���������Ч��" +
                "    ���Լ���ͱ�Э�����ݻ���ִ�з����κ����飬˫��Ӧ�����Ѻ�Э�̽����Э�̲���ʱ���κ�һ���������й�ϽȨ���л����񹲺͹���½������Ժ�������ϡ�" +
                "    <h5> ��12�� ���� </h5>" +
                "    <p>" +
                "        <strong>12.1</strong>������վ��������ָ����������������ɻ򱸰��ľ�����վ��Ӫ���塣</p>" +

                "    <p>" +
                "        <strong>12.2</strong>���������û��������ߵĺϷ�Ȩ������Э�鼰����վ�Ϸ����ĸ�������������������ݣ�����Ϊ�˸��õġ����ӱ�����Ϊ�û����������ṩ���񡣱�վ��ӭ�û����������������ͽ��飬���������Ľ��ܲ���ʱ�޸ı�Э�鼰��վ�ϵĸ������" +
                "    </p>" +

                "    <p>" +
                "        <strong>12.3</strong><span>��Э���������Ժ��塢�Ӵ֡��»��ߡ�б��ȷ�ʽ������ʶ��������û������Ķ���</span></p>" +
                "    <p>" +
                "        <strong>12.4</strong><span>�������Э���·���\"ͬ�Ⲣ����\"��ť����Ϊ����ȫ���ܱ�Э�飬�ڵ��֮ǰ�����ٴ�ȷ����֪Ϥ����ȫ��ⱾЭ���ȫ�����ݡ�</span></p>" +
                "</div>" +
                "      <div class=\"btnt\">" +
                "         <input  class=\"btn-img\"  type=\''button\" value='ͬ�Ⲣ����' onclick='protocolReg();'/>" +
                "     </div>" +
                "</div>" +
                "</div>" +
                "</div>",
            _autoReposi: true
        });
    });
});

function showHideProtocol() {
    var protocolNode = $('.protocol-box');
    if (!protocolNode.is(':hidden')) {
        protocolNode.hide();
    } else {
        protocolNode.show();
    }
    return false;
}

function validateRegName() {
    var loginName = $("#regName").val();
    if (validateRules.isNull(loginName) || loginName == '����/�û���/�ֻ���') {
        $("#regName").val("");
        $("#regName").attr({ "class": "text highlight2" });
        $("#regName_error").html("����������/�û���/�ֻ���").show().attr({ "class": "error" });
        return false;
    }
    return true;
}
$("#regist .tab li").hover(function () {
    if ($(this).hasClass("curr")) {
    } else {
        $(this).addClass("new");
    }
}, function () {
    if ($(this).hasClass("curr")) {
    } else {
        $(this).removeClass("new");
    }
})

$("#registsubmit").hover(function () {
    $(this).addClass("hover-btn")
}, function () {

    $(this).removeClass("hover-btn")
})