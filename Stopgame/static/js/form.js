function postRefreshPage () {
  var theForm, from_year_input, to_year_input, count_input;
  theForm = document.createElement('form');
  theForm.action = "search_result/";
  theForm.method = 'POST';

  from_year_input = document.createElement('input');
  from_year_input.type = 'hidden';
  from_year_input.name = 'from_year_input';
  from_year_input.value = fromValue.innerHTML;

  to_year_input = document.createElement('input');
  to_year_input.type = 'hidden';
  to_year_input.name = 'to_year_input';
  to_year_input.value = toValue.innerHTML;

  count_input = document.createElement('input');
  count_input.type = 'hidden';
  count_input.name = 'count_input';
  count_input.value = countValue.value;

  theForm.appendChild(from_year_input);
  theForm.appendChild(to_year_input);
  theForm.appendChild(count_input);
  document.getElementById('hidden_form_container').appendChild(theForm);
  theForm.submit();
}

const countValue = document.querySelector('#countValue');