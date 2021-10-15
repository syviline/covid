let canvas = document.querySelector('#canvas')
let ctx = canvas.getContext('2d')


// let newcases = {}
// let i = 0
// Object.keys(cases).forEach(key => {
//     if (i % 5 == 0) {
//         newcases[key] = cases[key]
//     }
//     i++;
// })

// test = () => {
//     chart.destroy()
//     chart = new Chart(ctx, {
//     type: 'bar',
//     data: {
//         labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
//         datasets: [{
//             label: '# of Votes',
//             data: [12, 19, 3, 5, 2, 3],
//             backgroundColor: [
//                 'rgba(255, 99, 132, 0.2)',
//                 'rgba(54, 162, 235, 0.2)',
//                 'rgba(255, 206, 86, 0.2)',
//                 'rgba(75, 192, 192, 0.2)',
//                 'rgba(153, 102, 255, 0.2)',
//                 'rgba(255, 159, 64, 0.2)'
//             ],
//             borderColor: [
//                 'rgba(255, 99, 132, 1)',
//                 'rgba(54, 162, 235, 1)',
//                 'rgba(255, 206, 86, 1)',
//                 'rgba(75, 192, 192, 1)',
//                 'rgba(153, 102, 255, 1)',
//                 'rgba(255, 159, 64, 1)'
//             ],
//             borderWidth: 2,
//         }]
//     },
//     options: {
//         scales: {
//             y: {
//                 beginAtZero: true
//             },
//             interaction: {
//                 mode: 'nearest'
//             }
//         }
//     }
// })
// }

newcases = {}

let chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: Object.keys(newcases),
        datasets: [{
            label: 'Случаев заражения',
            data: Object.values(newcases),
            borderWidth: 2,
            pointRadius: 0,
            backgroundColor: 'rgb(180, 0, 0)',
            borderColor: 'rgb(180, 0, 0)',
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true
            }
        }, hover: {
            mode: 'nearest',
            intersect: true
        }, interaction: {
            intersect: false
        }
    }
})

let countryListItem = document.querySelector('.country-list')
let searchBar = document.querySelector('#search')
let countryChoiceItem = document.querySelector('.country-choice')

function toggleCountryChoice() {
    if (countryChoiceItem.classList.contains('disabled')) {
        countryChoiceItem.classList.remove('disabled')
    } else {
        countryChoiceItem.classList.add('disabled')
    }
}

function searchUpdate() {
    countryListItem.innerHTML = ''
    let val = searchBar.value.toLowerCase()
    let newobj = {}
    Object.keys(countries).forEach(key => {
        if (countries[key].toLowerCase().includes(val)) {
            let a = document.createElement('a')
            a.innerText = countries[key]
            a.attributes['href'] = key
            countryListItem.appendChild(a)
        }
    });

}