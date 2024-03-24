const getRandomSubArray = (arr, size) => {
    let shuffled = arr.slice(0), i = arr.length, temp, index;
    while (i--) {
        index = Math.floor((i+1)* Math.random())
        temp = shuffled[index]
        shuffled[index] = shuffled[i]
        shuffled[i] = temp
    }
    return shuffled.slice(0, size)
}

const convertNewsDate = (news_date) => {
    return new Date(news_date).toLocaleString('vi', {month: 'long', year: 'numeric'})
}

export { getRandomSubArray, convertNewsDate }