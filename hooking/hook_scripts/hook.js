Interceptor.attach(Module.findExportByName("kernel32.dll", "LoadLibraryA"), {
    onEnter:function(args) {
        send('connect called');
    }
});
