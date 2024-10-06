def Login():
       return
Div(
    Nav(
        Div(
            Div(
                Button(
                    Div(
                        Span(
                            Img(alt='Alicia Koch', src='https://avatar.vercel.sh/personal.png', cls='aspect-square h-full w-full grayscale'),
                            cls='relative flex h-5 w-5 shrink-0 overflow-hidden rounded-full'
                        ),
                        Span('Alicia Koch', cls=''),
                        cls='flex flex-1 items-center gap-2'
                    ),
                    Svg(
                        Path(d='M4.93179 5.43179C4.75605 5.60753 4.75605 5.89245 4.93179 6.06819C5.10753 6.24392 5.39245 6.24392 5.56819 6.06819L7.49999 4.13638L9.43179 6.06819C9.60753 6.24392 9.89245 6.24392 10.0682 6.06819C10.2439 5.89245 10.2439 5.60753 10.0682 5.43179L7.81819 3.18179C7.73379 3.0974 7.61933 3.04999 7.49999 3.04999C7.38064 3.04999 7.26618 3.0974 7.18179 3.18179L4.93179 5.43179ZM10.0682 9.56819C10.2439 9.39245 10.2439 9.10753 10.0682 8.93179C9.89245 8.75606 9.60753 8.75606 9.43179 8.93179L7.49999 10.8636L5.56819 8.93179C5.39245 8.75606 5.10753 8.75606 4.93179 8.93179C4.75605 9.10753 4.75605 9.39245 4.93179 9.56819L7.18179 11.8182C7.35753 11.9939 7.64245 11.9939 7.81819 11.8182L10.0682 9.56819Z', fill='currentColor', fill_rule='evenodd', clip_rule='evenodd'),
                        width='15',
                        height='15',
                        viewbox='0 0 15 15',
                        fill='none',
                        xmlns='http://www.w3.org/2000/svg',
                        aria_hidden='true',
                        cls='h-4 w-4 flex-none opacity-50'
                    ),
                    type='button',
                    cls='uk-button uk-button-default w-full'
                ),
                Div(
                    Ul(
                        Li('Personal Account', cls='uk-nav-header'),
                        Li(
                            A(
                                Div(
                                    Span(
                                        Img(alt='Alicia Koch', src='https://avatar.vercel.sh/personal.png', cls='aspect-square h-full w-full grayscale'),
                                        cls='relative flex h-5 w-5 shrink-0 overflow-hidden rounded-full'
                                    ),
                                    Span('Alicha Koch', cls=''),
                                    cls='flex flex-1 items-center gap-2'
                                ),
                                Svg(
                                    Path(d='M20 6 9 17l-5-5'),
                                    xmlns='http://www.w3.org/2000/svg',
                                    width='16',
                                    height='16',
                                    viewbox='0 0 24 24',
                                    fill='none',
                                    stroke='currentColor',
                                    stroke_width='2',
                                    stroke_linecap='round',
                                    stroke_linejoin='round',
                                    cls='lucide lucide-check'
                                ),
                                href='#demo',
                                uk_toggle='',
                                cls='uk-drop-close justify-between'
                            ),
                            cls='uk-active'
                        ),
                        Li(cls='mt-3'),
                        Li('Teams', cls='uk-nav-header'),
                        Li(
                            A(
                                Div(
                                    Span(
                                        Img(alt='Alicia Koch', src='https://avatar.vercel.sh/personal.png', cls='aspect-square h-full w-full grayscale'),
                                        cls='relative flex h-5 w-5 shrink-0 overflow-hidden rounded-full'
                                    ),
                                    Span('Acme Inc.', cls=''),
                                    cls='flex flex-1 items-center gap-2'
                                ),
                                href='#demo',
                                uk_toggle='',
                                cls='uk-drop-close justify-between'
                            )
                        ),
                        Li(
                            A(
                                Div(
                                    Span(
                                        Img(alt='Alicia Koch', src='https://avatar.vercel.sh/personal.png', cls='aspect-square h-full w-full grayscale'),
                                        cls='relative flex h-5 w-5 shrink-0 overflow-hidden rounded-full'
                                    ),
                                    Span('Monster Inc.', cls=''),
                                    cls='flex flex-1 items-center gap-2'
                                ),
                                href='#demo',
                                uk_toggle='',
                                cls='uk-drop-close justify-between'
                            )
                        ),
                        Li(cls='uk-nav-divider'),
                        Li(
                            A(
                                Svg(
                                    Circle(cx='12', cy='12', r='10'),
                                    Path(d='M8 12h8'),
                                    Path(d='M12 8v8'),
                                    xmlns='http://www.w3.org/2000/svg',
                                    width='16',
                                    height='16',
                                    viewbox='0 0 24 24',
                                    fill='none',
                                    stroke='currentColor',
                                    stroke_width='2',
                                    stroke_linecap='round',
                                    stroke_linejoin='round',
                                    cls='lucide lucide-circle-plus mr-2'
                                ),
                                'Create a Team',
                                href='#demo',
                                uk_toggle='',
                                cls='uk-drop-close'
                            )
                        ),
                        cls='uk-dropdown-nav uk-nav'
                    ),
                    uk_dropdown='mode: click; pos: bottom-center',
                    cls='uk-dropdown uk-drop w-[200px]'
                ),
                cls='uk-navbar-item w-[200px]'
            ),
            Ul(
                Li(
                    A('Overview', href='#demo', uk_toggle=''),
                    cls='uk-active'
                ),
                Li(
                    A('Customers', href='#demo', uk_toggle='')
                ),
                Li(
                    A('Products', href='#demo', uk_toggle='')
                ),
                Li(
                    A('Settings', href='#demo', uk_toggle='')
                ),
                cls='uk-navbar-nav gap-x-4 lg:gap-x-6'
            ),
            cls='uk-navbar-left gap-x-4 lg:gap-x-6'
        ),
        Div(
            Div(
                Input(placeholder='Search', type='text', cls='uk-input'),
                cls='uk-navbar-item w-[150px] lg:w-[300px]'
            ),
            Div(
                A(
                    Span(
                        Img(alt='@shadcn', src='https://api.dicebear.com/8.x/lorelei/svg?seed=sveltecult', cls='aspect-square h-full w-full'),
                        cls='relative flex h-8 w-8 shrink-0 overflow-hidden rounded-full'
                    ),
                    href='#',
                    cls='inline-flex h-8 w-8 items-center justify-center rounded-full bg-accent ring-ring focus:outline-none focus-visible:ring-1'
                ),
                Div(
                    Ul(
                        Li(
                            Div(
                                P('sveltecult', cls='text-sm font-medium leading-none'),
                                P('leader@sveltecult.com', cls='text-xs leading-none text-muted-foreground'),
                                cls='flex flex-col space-y-1'
                            ),
                            cls='px-2 py-1.5 text-sm'
                        ),
                        Li(cls='uk-nav-divider'),
                        Li(
                            A(
                                'Profile',
                                Span('⇧⌘P', cls='ml-auto text-xs tracking-widest opacity-60'),
                                href='#demo',
                                uk_toggle='',
                                cls='uk-drop-close justify-between'
                            )
                        ),
                        Li(
                            A(
                                'Billing',
                                Span('⌘B', cls='ml-auto text-xs tracking-widest opacity-60'),
                                href='#demo',
                                uk_toggle='',
                                cls='uk-drop-close justify-between'
                            )
                        ),
                        Li(
                            A(
                                'Settings',
                                Span('⌘S', cls='ml-auto text-xs tracking-widest opacity-60'),
                                href='#demo',
                                uk_toggle='',
                                cls='uk-drop-close justify-between'
                            )
                        ),
                        Li(
                            A('New Team', href='#demo', uk_toggle='', cls='uk-drop-close justify-between')
                        ),
                        Li(cls='uk-nav-divider'),
                        Li(
                            A('Logout', href='#demo', uk_toggle='', cls='uk-drop-close justify-between')
                        ),
                        cls='uk-dropdown-nav uk-nav'
                    ),
                    uk_dropdown='mode: click; pos: bottom-right',
                    cls='uk-dropdown uk-drop'
                ),
                cls='uk-navbar-item'
            ),
            cls='uk-navbar-right gap-x-4 lg:gap-x-6'
        ),
        uk_navbar='',
        cls='uk-navbar'
    ),
    cls='border-b border-border px-4'
)

Div(
    Div(
        H2('Dashboard', cls='text-3xl font-bold tracking-tight'),
        Div(
            Button(
                Div(
                    Svg(
                        Path(d='M8 2v4'),
                        Path(d='M16 2v4'),
                        Rect(width='18', height='18', x='3', y='4', rx='2'),
                        Path(d='M3 10h18'),
                        Path(d='M8 14h.01'),
                        Path(d='M12 14h.01'),
                        Path(d='M16 14h.01'),
                        Path(d='M8 18h.01'),
                        Path(d='M12 18h.01'),
                        Path(d='M16 18h.01'),
                        xmlns='http://www.w3.org/2000/svg',
                        width='16',
                        height='16',
                        viewbox='0 0 24 24',
                        fill='none',
                        stroke='currentColor',
                        stroke_width='2',
                        stroke_linecap='round',
                        stroke_linejoin='round',
                        cls='lucide lucide-calendar-days'
                    ),
                    'Jan 20, 2024 - Feb 09, 2024',
                    uk_toggle='#demo',
                    cls='flex gap-x-2'
                ),
                cls='uk-button uk-button-default w-[260px]'
            ),
            Button('Download', uk_toggle='#demo', cls='uk-button uk-button-primary'),
            cls='flex items-center space-x-2'
        ),
        cls='flex items-center justify-between space-y-2'
    ),
    Div(
        Ul(
            Li(
                A('Overview', href='#demo', uk_toggle=''),
                cls='uk-active'
            ),
            Li(
                A('Analytics', href='#demo', uk_toggle='')
            ),
            Li(
                A('Reports', href='#demo', uk_toggle='')
            ),
            Li(
                A('Notifications', href='#demo', uk_toggle='')
            ),
            cls='uk-tab-alt max-w-96'
        ),
        Div(
            Div(
                Div(
                    H3('Total Revenue', cls='text-sm font-medium tracking-tight'),
                    Svg(
                        Path(d='M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6'),
                        xmlns='http://www.w3.org/2000/svg',
                        viewbox='0 0 24 24',
                        fill='none',
                        stroke='currentColor',
                        stroke_linecap='round',
                        stroke_linejoin='round',
                        stroke_width='2',
                        cls='h-4 w-4 text-muted-foreground'
                    ),
                    cls='uk-card-header flex flex-row items-center justify-between'
                ),
                Div(
                    Div('$45,231.89', cls='text-2xl font-bold'),
                    P('+20.1% from last month', cls='text-xs text-muted-foreground'),
                    cls='uk-card-body pt-0'
                ),
                cls='uk-card'
            ),
            Div(
                Div(
                    H3('Subscriptions', cls='text-sm font-medium tracking-tight'),
                    Svg(
                        Path(d='M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2'),
                        Circle(cx='9', cy='7', r='4'),
                        Path(d='M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75'),
                        xmlns='http://www.w3.org/2000/svg',
                        viewbox='0 0 24 24',
                        fill='none',
                        stroke='currentColor',
                        stroke_linecap='round',
                        stroke_linejoin='round',
                        stroke_width='2',
                        cls='h-4 w-4 text-muted-foreground'
                    ),
                    cls='uk-card-header flex flex-row items-center justify-between'
                ),
                Div(
                    Div('+2350', cls='text-2xl font-bold'),
                    P('+180.1% from last month', cls='text-xs text-muted-foreground'),
                    cls='uk-card-body pt-0'
                ),
                cls='uk-card'
            ),
            Div(
                Div(
                    H3('Sales', cls='text-sm font-medium tracking-tight'),
                    Svg(
                        Rect(width='20', height='14', x='2', y='5', rx='2'),
                        Path(d='M2 10h20'),
                        xmlns='http://www.w3.org/2000/svg',
                        viewbox='0 0 24 24',
                        fill='none',
                        stroke='currentColor',
                        stroke_linecap='round',
                        stroke_linejoin='round',
                        stroke_width='2',
                        cls='h-4 w-4 text-muted-foreground'
                    ),
                    cls='uk-card-header flex flex-row items-center justify-between'
                ),
                Div(
                    Div('+12,234', cls='text-2xl font-bold'),
                    P('+19% from last month', cls='text-xs text-muted-foreground'),
                    cls='uk-card-body pt-0'
                ),
                cls='uk-card'
            ),
            Div(
                Div(
                    H3('Active Now', cls='text-sm font-medium tracking-tight'),
                    Svg(
                        Path(d='M22 12h-4l-3 9L9 3l-3 9H2'),
                        xmlns='http://www.w3.org/2000/svg',
                        viewbox='0 0 24 24',
                        fill='none',
                        stroke='currentColor',
                        stroke_linecap='round',
                        stroke_linejoin='round',
                        stroke_width='2',
                        cls='h-4 w-4 text-muted-foreground'
                    ),
                    cls='uk-card-header flex flex-row items-center justify-between'
                ),
                Div(
                    Div('+573', cls='text-2xl font-bold'),
                    P('+201 since last hour', cls='text-xs text-muted-foreground'),
                    cls='uk-card-body pt-0'
                ),
                cls='uk-card'
            ),
            cls='grid grid-cols-2 gap-4 lg:grid-cols-4'
        ),
        Div(
            Div(
                Div(
                    Svg(
                        Circle(cx='12', cy='12', r='10'),
                        Line(x1='12', x2='12', y1='8', y2='12'),
                        Line(x1='12', x2='12.01', y1='16', y2='16'),
                        xmlns='http://www.w3.org/2000/svg',
                        width='16',
                        height='16',
                        viewbox='0 0 24 24',
                        fill='none',
                        stroke='currentColor',
                        stroke_width='2',
                        stroke_linecap='round',
                        stroke_linejoin='round',
                        cls='lucide lucide-circle-alert'
                    ),
                    'Graph not available',
                    cls='flex flex-1 items-center justify-center gap-x-2 text-destructive'
                ),
                cls='uk-card flex min-h-64 items-center justify-center lg:col-span-4'
            ),
            Div(
                Div(
                    H3('Recent Sales', cls='font-semibold leading-none tracking-tight'),
                    P('You made 265 sales this month.', cls='text-sm text-muted-foreground'),
                    cls='uk-card-header'
                ),
                Div(
                    Div(
                        '{\r\n                [\r\n                  {\r\n                    name: "Olivia Martin",\r\n                    email: "olivia.martin@email.com",\r\n                    amount: "+$1,999.00",\r\n                  },\r\n                  {\r\n                    name: "Jackson Lee",\r\n                    email: "jackson.lee@email.com",\r\n                    amount: "+$39.00",\r\n                  },\r\n                  {\r\n                    name: "Isabella Nguyen",\r\n                    email: "isabella.nguyen@email.com",\r\n                    amount: "+$299.00",\r\n                  },\r\n                  {\r\n                    name: "William Kim",\r\n                    email: "will@email.com",\r\n                    amount: "+$99.00",\r\n                  },\r\n                  {\r\n                    name: "Sofia Davis",\r\n                    email: "sofia.davis@email.com",\r\n                    amount: "+$39.00",\r\n                  },\r\n                ].map((a) => (',
                        Div(
                            Span(
                                Img(alt='Avatar', src='{`https://api.dicebear.com/8.x/lorelei/svg?seed=${a.name}`}', cls='aspect-square h-full w-full'),
                                cls='relative flex h-9 w-9 shrink-0 overflow-hidden rounded-full bg-accent'
                            ),
                            Div(
                                P('{a.name}', cls='text-sm font-medium leading-none'),
                                P('{a.email}', cls='text-sm text-muted-foreground'),
                                cls='ml-4 space-y-1'
                            ),
                            Div('{a.amount}', cls='ml-auto font-medium'),
                            cls='flex items-center'
                        ),
                        '))\r\n              }',
                        cls='space-y-8'
                    ),
                    cls='uk-card-body pt-0'
                ),
                cls='uk-card lg:col-span-3'
            ),
            cls='grid gap-4 lg:grid-cols-7'
        ),
        cls='space-y-4'
    ),
    cls='flex-1 space-y-4 p-8 pt-6'
)
