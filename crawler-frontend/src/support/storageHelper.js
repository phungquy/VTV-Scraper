export const saveNewsToStorage = (news) => {
    localStorage.setItem("news", JSON.stringify(news))
}

export const removeNewsFromStorage = () => {
    localStorage.removeItem("news");
}