package("quickjs-maye")

    set_homepage("https://bellard.org/quickjs/")
    set_description("QuickJS is a small and embeddable Javascript engine")

    --if is_plat("windows") then
        add_urls("https://github.com/maye174/quickjs.git")
        add_versions("2021.03.27", "da68f587ee6b2fedb450b78c6dd56e3d03b3a158")
    --else
        --add_urls("https://github.com/bellard/quickjs.git")
        --add_versions("2021.03.27", "b5e62895c619d4ffc75c9d822c8d85f1ece77e5b")
    --end

    if is_plat("linux", "macosx", "iphoneos", "cross") then
        add_syslinks("pthread", "dl", "m")
    elseif is_plat("android") then
        add_syslinks("dl", "m")
    end
    
    on_install("linux", "macosx", "iphoneos", "android", "mingw", "cross", function (package)
        io.writefile("xmake.lua", ([[
            add_rules("mode.debug", "mode.release")
            target("quickjs")
                set_kind("$(kind)")
                add_files("src/quickjs*.c", "src/cutils.c", "src/lib*.c")
                add_headerfiles("src/quickjs-libc.h")
                add_headerfiles("src/quickjs.h")
                add_installfiles("src/*.js", {prefixdir = "share"})
                set_languages("c99")
                add_defines("CONFIG_VERSION=\"%s\"", "_GNU_SOURCE")
                add_defines("CONFIG_BIGNUM")
                if is_plat("windows", "mingw") then
                    add_defines("__USE_MINGW_ANSI_STDIO")
                end
        ]]):format(package:version_str()))
        local configs = {}
        if package:config("shared") then
            configs.kind = "shared"
        end
        if package:is_plat("cross") then
            io.replace("src/quickjs.c", "#define CONFIG_PRINTF_RNDN", "")
        end
        import("package.tools.xmake").install(package, configs)
    end)

    on_install("windows", function (package)
        local configs = {}
        if package:config("shared") then
            configs.kind = "shared"
        end
        import("package.tools.xmake").install(package, configs)
    end)

    on_test(function (package)
        assert(package:has_cfuncs("JS_NewRuntime", {includes = "src/quickjs.h"}))
    end)