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
}