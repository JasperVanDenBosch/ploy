

function makeFieldsHumanReadable() {
    $('.datetime').each(function() {
        $( this ).text(function (i, txt) {
            return moment(txt).fromNow();
        });
    });
}

makeFieldsHumanReadable();

