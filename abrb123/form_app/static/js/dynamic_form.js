$(document).ready(function() {
    let fieldCount = 1;
    
    $('#add-field').click(function() {
        const newField = `
            <div class="field-wrapper">
                <input type="text" name="name${fieldCount}" placeholder="Введите имя">
                <button type="button" class="remove-field">Удалить</button>
            </div>
        `;
        $('#fields-container').append(newField);
        fieldCount++;
    });
    
    $(document).on('click', '.remove-field', function() {
        $(this).parent().remove();
    });
});