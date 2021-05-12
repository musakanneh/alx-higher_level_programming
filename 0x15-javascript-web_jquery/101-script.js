$(function() {
    $('#add_item').click(function() {
        $('ul.my_list').append('<li>Item</li>');
    });
});

$(function() {
    $('#remove_item').click(function() {
        $('ul.my_list li').last().remove();
    });
});

$(function() {
    $('#clear_list').click(function() {
        $('ul.my_list').empty();
    });
});