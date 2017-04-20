KindEditor.ready(function(K){
    K.create('textarea[name=content]',{
        width:'700px',
        height:'500px',
        uploadJson: '/admin/upload/kindeditor',
    })
});