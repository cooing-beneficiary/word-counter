// times-table.js
// <script src="static/times-table.js"></script>
console.log('loaded');

active_col = 1;
active_row = 1;
active_prod = 1;

data_cells = document.getElementsByTagName('td');

// Add click listener to top row of times table.
for (var i = 0; i < 10; i++) {
	data_cells[i].addEventListener('click', function() {
        active_col = this.innerHTML;
        console.log(active_row);
        console.log(active_col);
        console.log(active_row * active_col);
        data_cells[active_row * active_col - 1].style.backgroundColor="blue";
	});	
}

// Add click listener to side row of times table.
for (var i = 10; i <= 100; i += 10) {
	data_cells[i].addEventListener('click', function() {
        active_row = this.innerHTML;
        console.log(active_row);
        console.log(active_col);
        console.log(active_row * active_col);
        data_cells[active_row * active_col - 1].style.backgroundColor="blue";
	});
}
