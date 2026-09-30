async function delay(seconds) {
    return new Promise(function(resolve, reject) {
        setTimeout(resolve, seconds * 1000);
    })
}


async function load_data() {
    const limit = 100;
    let offset = 0;
    let all_developers = [];
    while (true) {
        console.log('offset = ', offset);
        const response = await fetch(`https://xn--80az8a.xn--d1aqf.xn--p1ai/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B/api/erz/main/filter?offset=${offset}&limit=${limit}&sortField=devShortNm&sortType=asc&objStatus=0`)
        const data = await response.json();
        const count = data.data.count;
        const developers = data.data.developers;
        all_developers = all_developers.concat(developers);
        if (developers.length < limit) {
            break
        }
        offset += limit;
        await delay(2);
    }
    return all_developers;
}


async function main() {
    const developers = await load_data();
    console.log(developers.length)
    const jsonStringify = JSON.stringify(developers, null, 4);
    const blob = new Blob([jsonStringify], {type: "application/json"});
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'developers.json';

    document.body.appendChild(link);
    link.click();
}

main()
