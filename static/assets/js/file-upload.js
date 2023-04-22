(function($) {
  'use strict';
  $(function() {
    $('.file-upload-browse').on('click', function() {
      var file = $(this).parent().parent().parent().find('.file-upload-default');
      file.trigger('click');
    });
    $('.file-upload-default').on('change', function() {
      $(this).parent().find('.file-upload-info').val($(this).val().replace(/C:\\fakepath\\/i, ''));
      let file_name=$(this).val().replace(/C:\\fakepath\\/i, '');
      $('.file-upload-default').val(file_name);
    });
  });
})(jQuery);