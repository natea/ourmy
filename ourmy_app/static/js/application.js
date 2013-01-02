$(document).ready(function() {
    $("a[rel=popover]")
        .popover({
            offset: 1
        })
        .click(function(e) {
            e.preventDefault()
        })
});
