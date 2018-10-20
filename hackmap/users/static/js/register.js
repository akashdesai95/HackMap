function openLogin() {
    let timeline = anime.timeline();

    timeline
        .add({
        targets: '.sign-up-form',
        opacity: 0,
    })
    .add({
        targets: '.login-form',
        opacity: 1,
    });
    document.getElementsByClassName('login-form')[0].style.display = 'block';
    document.getElementsByClassName('sign-up-form')[0].style.display = 'none';
}