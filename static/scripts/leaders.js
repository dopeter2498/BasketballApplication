function sortTable(col) {
  const table = document.getElementById('table');
  const rows = table.rows;
  const cols = [1, 2, 4];
  let newObj = createRowsObject(col);
  if (cols.indexOf(col) !== -1) {
    newObj.sort(rowSorter2);
    let list = [];
    for (let i = 0; i < newObj.length; i++) {
      list.push(newObj[i]['index']);
      let offset = 0;
      for (let j = 0; j < list.length; j++) {
        if (newObj[i]['index'] < list[j]) {
          offset++;
        }
      }
      rows[i+1].parentNode.insertBefore(rows[newObj[i]['index'] + 1 + offset], rows[i+1]);
    }
  } else {
    newObj.sort(rowSorter1);
    let list = [];
    for (let i = 0; i < newObj.length; i++) {
      list.push(newObj[i]['index']);
      let offset = 0;
      for (let j = 0; j < list.length; j++) {
        if (newObj[i]['index'] < list[j]) {
          offset++;
        }
      }
      rows[i+1].parentNode.insertBefore(rows[newObj[i]['index'] + 1 + offset], rows[i+1]);
    }
  }
  fixTableRowNums();
}

function fixTableRowNums() {
  const table = document.getElementById('table');
  const rows = table.rows;
  for (let i = 1; i < rows.length; i++) {
      const row = rows[i].getElementsByTagName('td')[0];
      row.innerHTML = i;
  }
}

function rowSorter1(a, b) {
  return a['data'] < b['data'];
}

function rowSorter2(a,b) {
  let i = 1;
  let same = false;
  while (true) {
    if (i === a['data'].length && i === b['data'].length) {
      same = true;
      break;
    } else if (i === a['data'].length) {
      break;
    } else if (i === b['data'].length) {
      return false;
    }
    if (a['data'][i] > b['data'][i]) {
      break;
    } else if (b['data'][i] > a['data'][i]) {
      return false;
    }
    i++;
  }
  if (same) {
    return a['data'][0] > b['data'][0];
  }
  return true;
}

function createRowsObject(col) {
  const table = document.getElementById('table');
  const rows = table.rows;
  const rowsObj = [];
  const cols = [1, 2, 4];
  if (cols.indexOf(col) !== -1) {
    for (let i = 1; i < rows.length; i++) {
      const row = rows[i].getElementsByTagName('td')[col];
      rowsObj.push({
        'data': [
          row.innerHTML.toLowerCase().split(' ')[0], 
          row.innerHTML.toLowerCase().split(' ').slice(1)
        ],
        'index': i-1
      });
    }
  } else {
    for (let i = 1; i < rows.length; i++) {
      const row = rows[i].getElementsByTagName('td')[col];
      let data = -1;
      if (row.innerHTML !== 'nan') {
        data = parseFloat(row.innerHTML);
      }
      rowsObj.push({
        'data': data,
        'index': i-1
      });
    }
  }
  return rowsObj;
}
