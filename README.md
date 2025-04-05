If the opponent’s generosity looks suspicious — either too much or too little — betray.
If they keep being kind in a row? Cooperate, but watch your pockets.
Everyone else? You get one chance, that’s it.

What's the plan, fam?
Counting 0s like a tax audit:

Tally how many times we’ve defected (0) vs how many times the opponent has.

This is our way of measuring generosity — or lack thereof.

Snitch Check:

If the opponent suddenly drops 3 straight 1s (cooperating) like they found morality — we ain't falling for that. Robin’s like “huh, what’s this kindness?” and returns a 1 back (cooperate).

Basically: If they're butterin' us up, we play nice for now.

Dynamic Gap Hustle:

There’s now a twist: we calculate a dynamic_gap, which stays at 0 for now (might be tuned later).

More importantly, we calculate dynamic_gap_less = total_rounds // 4, which grows over time.

This adds some spicy flexibility to how tolerant we are before deciding to rob.

Robbery Logic:

If the opponent has been more generous than us (more 0s) by dynamic_gap or more — steal! (play 0)

If they’ve been way stingier (like, wow stingier — by more than dynamic_gap_less) — steal! (play 0 again)

Basically: If they act too nice or too mean, we rob ‘em blind.

Otherwise:
If their behavior seems chill and kinda balanced, Robin shrugs and cooperates (1). Sometimes even Robin gets tired of mugging.

