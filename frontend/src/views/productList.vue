<template>
    <div class="row" v-for="(row, index) in finalList">
        <div class="drip-card" v-for="item in row">
            <div class="image-box">
                <img class="item-img"  :src="item.image"/>
            </div>
            <div class="title-box">
                <span class="item-title">{{ item.title }}</span>
            </div>
            <div class="desc-box">
                <span class="item-desc">{{ item.description }}</span>
            </div>
            <div class="centered">
                <button class="item-button" href="item.link">See the sauce</button>
            </div>
        </div>
    </div>
</template>

<script>

import { CCard } from "@coreui/vue/";

export default {
    name: "productList",
    data() {
        return {
            itemList: [
                {
                    title: "Supreme\u00ae/The North Face\u00ae ",
                    price: "\u20ac438",
                    image: "https://assets.supremenewyork.com/250918/ma/nABDsXy1BSc.jpg",
                    link: "https://www.supremenewyork.com/shop/jackets/mqg8xwafz/zneigxfu9",
                    category: "jackets",
                    description:
                        "Waterproof 3-layer recycled nylon shell with fully sealed seams and printed logo tricot backing. Full zip closure with on seam zip hand pockets. Zip pockets at front and chest. Zip stash pocket at sleeve with interior microfiber goggle wipe. Interior elastic mesh pocket and two-way pit zips. Interior elastic shockcord at fixed hood and hem with velcro tab adjusters at cuffs.  Transparent watch window at cuff. Embroidered logos at chest, hood and back. Logo patches on sleeve. Made exclusively for Supreme.",
                    color: "Times Square",
                    available: true,
                    sizes: ["Small", "Medium", "Large"],
                },
                {
                    title: "Supreme\u00ae/CCM\u00ae All Stars Hockey Jersey",
                    price: "\u20ac248",
                    image: "https://assets.supremenewyork.com/245786/ma/kip4qy2M40g.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/ks85xti3z/c9ukcjqzp",
                    category: "tops-sweaters",
                    description:
                        "Poly jersey with tackle twill logo appliqu\u00e9 at chest and back. Printed logo appliqu\u00e9 at lower front and tackle twill graphic appliqu\u00e9 at back. Embroidered tackle twill appliqu\u00e9 at sleeves and back hem. Athletic label at lower front. Made in Canada exclusively for Supreme.",
                    color: "Black",
                    available: true,
                    sizes: ["Small", "Medium", "Large", "XLarge", "XXL"],
                },
                {
                    title: "Drip Thermal",
                    price: "\u20ac98",
                    image: "https://assets.supremenewyork.com/249910/ma/YnqCCP4t3AQ.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/iz8pav59x/inrfkh2w8",
                    category: "tops-sweaters",
                    description: "Cotton blend waffle thermal with printed pattern.",
                    color: "White",
                    available: true,
                    sizes: ["Medium", "Large", "XLarge"],
                },
                {
                    title: "Layered Hooded L/S Top",
                    price: "\u20ac98",
                    image: "https://assets.supremenewyork.com/245795/ma/0RSd-7h9zyM.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/rpb0odr4m/kjl3hfaki",
                    category: "tops-sweaters",
                    description: "All cotton jersey with printed logos on sleeves.",
                    color: "Red",
                    available: true,
                    sizes: ["Large"],
                },
                {
                    title: "Supreme\u00ae/CCM\u00ae All Stars Hockey Jersey",
                    price: "\u20ac248",
                    image: "https://assets.supremenewyork.com/245783/ma/SQrUaJAABVI.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/ks85xti3z/o3xyngaec",
                    category: "tops-sweaters",
                    description:
                        "Poly jersey with tackle twill logo appliqu\u00e9 at chest and back. Printed logo appliqu\u00e9 at lower front and tackle twill graphic appliqu\u00e9 at back. Embroidered tackle twill appliqu\u00e9 at sleeves and back hem. Athletic label at lower front. Made in Canada exclusively for Supreme.",
                    color: "White",
                    available: true,
                    sizes: ["Small", "Medium", "Large", "XLarge", "XXL"],
                },
                {
                    title: "Drip Thermal",
                    price: "\u20ac98",
                    image: "https://assets.supremenewyork.com/249908/ma/c2ToOcg2Zcc.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/iz8pav59x/hhniyb6ec",
                    category: "tops-sweaters",
                    description: "Cotton blend waffle thermal with printed pattern.",
                    color: "Black",
                    available: true,
                    sizes: ["Small", "Medium", "Large", "XLarge"],
                },
                {
                    title: "Layered Hooded L/S Top",
                    price: "\u20ac98",
                    image: "https://assets.supremenewyork.com/245797/ma/RwAi9M6rShU.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/rpb0odr4m/g5uspqow4",
                    category: "tops-sweaters",
                    description: "All cotton jersey with printed logos on sleeves.",
                    color: "Black",
                    available: true,
                    sizes: ["Medium", "Large", "XLarge", "XXL"],
                },
                {
                    title: "Bones S/S Top",
                    price: "\u20ac78",
                    image: "https://assets.supremenewyork.com/250375/ma/mT_qtYvBYMg.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/w6unm89ti/sned0q9ow",
                    category: "tops-sweaters",
                    description:
                        "All cotton slub jersey crewneck with twill logo appliqu\u00e9 at chest. Athletic label at lower front.",
                    color: "Brown",
                    available: true,
                    sizes: ["XLarge"],
                },
                {
                    title: "Supreme\u00ae/The North Face\u00ae ",
                    price: "\u20ac68",
                    image: "https://assets.supremenewyork.com/250955/ma/7z3OXH8oab0.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/povuj3xq7/ljapc9b7o",
                    category: "tops-sweaters",
                    description:
                        "All cotton crewneck with embroidered logos on chest. Made exclusively for Supreme.",
                    color: "Yellow",
                    available: true,
                    sizes: ["Medium", "Large", "XLarge", "XXL"],
                },
                {
                    title: "Supreme\u00ae/The North Face\u00ae ",
                    price: "\u20ac68",
                    image: "https://assets.supremenewyork.com/250949/ma/uvWL_YSx35A.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/povuj3xq7/kjp0ct8ui",
                    category: "tops-sweaters",
                    description:
                        "All cotton crewneck with embroidered logos on chest. Made exclusively for Supreme.",
                    color: "Black",
                    available: false,
                    sizes: [],
                },
                {
                    title: "Supreme\u00ae/The North Face\u00ae ",
                    price: "\u20ac68",
                    image: "https://assets.supremenewyork.com/250951/ma/JUY5yBvY9so.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/povuj3xq7/q1lthnxa0",
                    category: "tops-sweaters",
                    description:
                        "All cotton crewneck with embroidered logos on chest. Made exclusively for Supreme.",
                    color: "Brown",
                    available: true,
                    sizes: ["Small", "Medium", "Large", "XLarge"],
                },
                {
                    title: "Supreme\u00ae/The North Face\u00ae",
                    price: "\u20ac238",
                    image: "https://assets.supremenewyork.com/250975/ma/lKmFSbvH9PE.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/xrqg60y8x/jw6qh275y",
                    category: "tops-sweaters",
                    description:
                        "Merino wool with knit logo pattern. Full zip closure and pouch pocket at lower front. Made exclusively for Supreme.",
                    color: "Pink",
                    available: false,
                    sizes: [],
                },
                {
                    title: "Elephant Skateboard",
                    price: "\u20ac66",
                    image: "https://assets.supremenewyork.com/247599/ma/cDzzDKrgjWY.jpg",
                    link: "https://www.supremenewyork.com/shop/skate/rgkuisnve/qs75m0dnq",
                    category: "skate",
                    description:
                        "Supreme skate deck with natural veneer and black top ply. Printed logo on bottom with printed World Famous and box logo on top. Original artwork by Shaun Crawford.",
                    color: 'White - 8" x 31.875" ',
                    available: true,
                    sizes: ["8 "],
                },
                {
                    title: "Elephant Skateboard",
                    price: "\u20ac66",
                    image: "https://assets.supremenewyork.com/247597/ma/89_Qem-7TSM.jpg",
                    link: "https://www.supremenewyork.com/shop/skate/rgkuisnve/fah6r81jk",
                    category: "skate",
                    description:
                        "Supreme skate deck with natural veneer and black top ply. Printed logo on bottom with printed World Famous and box logo on top. Original artwork by Shaun Crawford.",
                    color: 'Black - 8.25" x 32" ',
                    available: true,
                    sizes: ["8 1/4"],
                },
                {
                    title: "Elephant Skateboard",
                    price: "\u20ac66",
                    image: "https://assets.supremenewyork.com/247598/ma/TOAHC_FXe78.jpg",
                    link: "https://www.supremenewyork.com/shop/skate/rgkuisnve/rvnsaqr7b",
                    category: "skate",
                    description:
                        "Supreme skate deck with natural veneer and black top ply. Printed logo on bottom with printed World Famous and box logo on top. Original artwork by Shaun Crawford.",
                    color: 'Green - 8.125" x 32" ',
                    available: true,
                    sizes: ["8 1/8"],
                },
                {
                    title: "Supreme\u00ae/The North Face\u00ae",
                    price: "\u20ac238",
                    image: "https://assets.supremenewyork.com/250971/ma/Pa6ZNzcasZw.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/xrqg60y8x/j9zrxhtin",
                    category: "tops-sweaters",
                    description:
                        "Merino wool with knit logo pattern. Full zip closure and pouch pocket at lower front. Made exclusively for Supreme.",
                    color: "Black",
                    available: true,
                    sizes: ["Large"],
                },
                {
                    title: "Layered Hooded L/S Top",
                    price: "\u20ac98",
                    image: "https://assets.supremenewyork.com/245799/ma/TTeOd3Tkr2o.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/rpb0odr4m/b86qo1ch5",
                    category: "tops-sweaters",
                    description: "All cotton jersey with printed logos on sleeves.",
                    color: "Olive",
                    available: true,
                    sizes: ["Medium", "Large"],
                },
                {
                    title: "Layered Hooded L/S Top",
                    price: "\u20ac98",
                    image: "https://assets.supremenewyork.com/245801/ma/57bBeGi29WQ.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/rpb0odr4m/yo6gyswqz",
                    category: "tops-sweaters",
                    description: "All cotton jersey with printed logos on sleeves.",
                    color: "White",
                    available: true,
                    sizes: ["Large", "XLarge", "XXL"],
                },
                {
                    title: "Box Logo T-Shirt Skateboard",
                    price: "\u20ac66",
                    image: "https://assets.supremenewyork.com/247601/ma/kg9xTgvpPJg.jpg",
                    link: "https://www.supremenewyork.com/shop/skate/s5jp49wv2/ozb8jsg4e",
                    category: "skate",
                    description:
                        "Supreme skate deck with natural veneer and black top ply. Printed graphic on bottom with printed World Famous and box logo on top. Painted by Robby Rose. ",
                    color: 'White - 8.5" x 32"',
                    available: true,
                    sizes: ["8 1/2"],
                },
                {
                    title: "Supreme\u00ae/Spitfire\u00ae ",
                    price: "\u20ac48",
                    image: "https://assets.supremenewyork.com/247720/ma/IB9-_dOEUX4.jpg",
                    link: "https://www.supremenewyork.com/shop/skate/h4i5jtc6b/rvblcgmd4",
                    category: "skate",
                    description:
                        "Classic Spitfire\u00ae wheels with custom Supreme art. Each size sold separately as a set of four wheels. 52mm & 54mm wheels are classic 99D hard urethane. Made exclusively for Supreme.",
                    color: "White 52mm",
                    available: true,
                    sizes: ["52MM"],
                },
                {
                    title: "Supreme\u00ae/The North Face\u00ae ",
                    price: "\u20ac68",
                    image: "https://assets.supremenewyork.com/250953/ma/nC0eOJqcZTs.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/povuj3xq7/i0ya7dmph",
                    category: "tops-sweaters",
                    description:
                        "All cotton crewneck with embroidered logos on chest. Made exclusively for Supreme.",
                    color: "Purple",
                    available: true,
                    sizes: ["XXL"],
                },
                {
                    title: "Supreme\u00ae/Spitfire\u00ae ",
                    price: "\u20ac48",
                    image: "https://assets.supremenewyork.com/247714/ma/rfzWqznnu2k.jpg",
                    link: "https://www.supremenewyork.com/shop/skate/h4i5jtc6b/ssvcjo687",
                    category: "skate",
                    description:
                        "Classic Spitfire\u00ae wheels with custom Supreme art. Each size sold separately as a set of four wheels. 52mm & 54mm wheels are classic 99D hard urethane. Made exclusively for Supreme.",
                    color: "Swirl 54mm",
                    available: true,
                    sizes: ["54MM"],
                },
                {
                    title: "Supreme\u00ae/Nike\u00ae Air Force 1 Low",
                    price: "\u20ac128",
                    image: "https://assets.supremenewyork.com/247998/ma/aqXotkxJaFk.jpg",
                    link: "https://www.supremenewyork.com/shop/shoes/gxq0eu6dg/n3lsuwvz8",
                    category: "shoes",
                    description:
                        "Full-grain leather upper with perforated leather toe panel and DURAPLUSH lining. Co-branded footbed, lace lock and tongue label. Embroidered logos at eyestay and heel with debossed printed logo at side. Set of printed logo laces included. Made exclusively for Supreme. ",
                    color: "Black",
                    available: true,
                    sizes: [
                        "US 8 / UK 7",
                        "US 8.5 / UK 7.5",
                        "US 9 / UK 8",
                        "US 9.5 / UK 8.5",
                        "US 10 / UK 9",
                        "US 10.5 / UK 9.5",
                        "US 11 / UK 10",
                    ],
                },
                {
                    title: "Supreme\u00ae/Nike\u00ae Air Force 1 Low",
                    price: "\u20ac128",
                    image: "https://assets.supremenewyork.com/247989/ma/Z8P4Ma07U2k.jpg",
                    link: "https://www.supremenewyork.com/shop/shoes/gxq0eu6dg/brtipyd6s",
                    category: "shoes",
                    description:
                        "Full-grain leather upper with perforated leather toe panel and DURAPLUSH lining. Co-branded footbed, lace lock and tongue label. Embroidered logos at eyestay and heel with debossed printed logo at side. Set of printed logo laces included. Made exclusively for Supreme. ",
                    color: "White",
                    available: true,
                    sizes: ["US 12 / UK 11", "US 13 / UK 12"],
                },
                {
                    title: "Supreme\u00ae/Independent\u00ae Truck",
                    price: "\u20ac80",
                    image: "https://assets.supremenewyork.com/247730/ma/tgjDbiZPJLQ.jpg",
                    link: "https://www.supremenewyork.com/shop/skate/pn2s9lgz6/bsa0l1gn4",
                    category: "skate",
                    description:
                        "Classic Independent\u00ae truck with custom Supreme art. Each size sold separately as a pair of two trucks. Made exclusively for Supreme.",
                    color: "Silver",
                    available: true,
                    sizes: ["129 ", "139 ", "149 "],
                },
                {
                    title: "Supreme\u00ae/Nike\u00ae Air Force 1 Low",
                    price: "\u20ac150",
                    image: "https://assets.supremenewyork.com/248918/ma/Qqb2_7WGYoI.jpg",
                    link: "https://www.supremenewyork.com/shop/shoes/guarx76nw/twlsgaybj",
                    category: "shoes",
                    description:
                        "Full-grain Nubuck upper with perforated leather toe panel and DURAPLUSH lining. Co-branded footbed, lace lock and tongue label. Embroidered logos at eyestay and heel with debossed printed logo at side. Set of printed logo laces included. Made exclusively for Supreme.",
                    color: "Wheat",
                    available: true,
                    sizes: [
                        "US 8 / UK 7",
                        "US 8.5 / UK 7.5",
                        "US 9 / UK 8",
                        "US 9.5 / UK 8.5",
                        "US 10 / UK 9",
                        "US 10.5 / UK 9.5",
                        "US 11 / UK 10",
                        "US 11.5 / UK 10.5",
                        "US 12 / UK 11",
                        "US 13 / UK 12",
                    ],
                },
                {
                    title: "Supreme\u00ae/Hanes\u00ae Crew Socks (4 Pack)",
                    price: "\u20ac24",
                    image: "https://assets.supremenewyork.com/247743/ma/EDccMjVM8Q4.jpg",
                    link: "https://www.supremenewyork.com/shop/accessories/k57j632cd/wq5y31w2e",
                    category: "accessories",
                    description:
                        "Cotton blend Hanes\u00ae cushion comfort crew sock with jacquard logo at top.",
                    color: "Black",
                    available: true,
                    sizes: [],
                },
                {
                    title: "Supreme\u00ae/CCM\u00ae All Stars Hockey Jersey",
                    price: "\u20ac248",
                    image: "https://assets.supremenewyork.com/245786/ma/kip4qy2M40g.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/ks85xti3z/c9ukcjqzp?alt=1",
                    category: "tops-sweaters",
                    description:
                        "Poly jersey with tackle twill logo appliqu\u00e9 at chest and back. Printed logo appliqu\u00e9 at lower front and tackle twill graphic appliqu\u00e9 at back. Embroidered tackle twill appliqu\u00e9 at sleeves and back hem. Athletic label at lower front. Made in Canada exclusively for Supreme.",
                    color: "Black",
                    available: true,
                    sizes: ["Small", "Medium", "Large", "XLarge", "XXL"],
                },
                {
                    title: "Supreme\u00ae/The North Face\u00ae ",
                    price: "\u20ac438",
                    image: "https://assets.supremenewyork.com/250918/ma/nABDsXy1BSc.jpg",
                    link: "https://www.supremenewyork.com/shop/jackets/mqg8xwafz/zneigxfu9?alt=2",
                    category: "jackets",
                    description:
                        "Waterproof 3-layer recycled nylon shell with fully sealed seams and printed logo tricot backing. Full zip closure with on seam zip hand pockets. Zip pockets at front and chest. Zip stash pocket at sleeve with interior microfiber goggle wipe. Interior elastic mesh pocket and two-way pit zips. Interior elastic shockcord at fixed hood and hem with velcro tab adjusters at cuffs.  Transparent watch window at cuff. Embroidered logos at chest, hood and back. Logo patches on sleeve. Made exclusively for Supreme.",
                    color: "Times Square",
                    available: true,
                    sizes: ["Small", "Medium", "Large"],
                },
                {
                    title: "Supreme\u00ae/CCM\u00ae All Stars Hockey Jersey",
                    price: "\u20ac248",
                    image: "https://assets.supremenewyork.com/245786/ma/kip4qy2M40g.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/ks85xti3z/c9ukcjqzp?alt=0",
                    category: "tops-sweaters",
                    description:
                        "Poly jersey with tackle twill logo appliqu\u00e9 at chest and back. Printed logo appliqu\u00e9 at lower front and tackle twill graphic appliqu\u00e9 at back. Embroidered tackle twill appliqu\u00e9 at sleeves and back hem. Athletic label at lower front. Made in Canada exclusively for Supreme.",
                    color: "Black",
                    available: true,
                    sizes: ["Small", "Medium", "Large", "XLarge", "XXL"],
                },
                {
                    title: "Supreme\u00ae/CCM\u00ae All Stars Hockey Jersey",
                    price: "\u20ac248",
                    image: "https://assets.supremenewyork.com/245783/ma/SQrUaJAABVI.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/ks85xti3z/o3xyngaec?alt=1",
                    category: "tops-sweaters",
                    description:
                        "Poly jersey with tackle twill logo appliqu\u00e9 at chest and back. Printed logo appliqu\u00e9 at lower front and tackle twill graphic appliqu\u00e9 at back. Embroidered tackle twill appliqu\u00e9 at sleeves and back hem. Athletic label at lower front. Made in Canada exclusively for Supreme.",
                    color: "White",
                    available: true,
                    sizes: ["Small", "Medium", "Large", "XLarge", "XXL"],
                },
                {
                    title: "Supreme\u00ae/The North Face\u00ae ",
                    price: "\u20ac438",
                    image: "https://assets.supremenewyork.com/250913/ma/PJYNnPAgL0I.jpg",
                    link: "https://www.supremenewyork.com/shop/jackets/mqg8xwafz/mivmpb64k?alt=1",
                    category: "jackets",
                    description:
                        "Waterproof 3-layer recycled nylon shell with fully sealed seams and printed logo tricot backing. Full zip closure with on seam zip hand pockets. Zip pockets at front and chest. Zip stash pocket at sleeve with interior microfiber goggle wipe. Interior elastic mesh pocket and two-way pit zips. Interior elastic shockcord at fixed hood and hem with velcro tab adjusters at cuffs.  Transparent watch window at cuff. Embroidered logos at chest, hood and back. Logo patches on sleeve. Made exclusively for Supreme.",
                    color: "Grey",
                    available: false,
                    sizes: [],
                },
                {
                    title: "Supreme\u00ae/The North Face\u00ae ",
                    price: "\u20ac438",
                    image: "https://assets.supremenewyork.com/250913/ma/PJYNnPAgL0I.jpg",
                    link: "https://www.supremenewyork.com/shop/jackets/mqg8xwafz/mivmpb64k?alt=0",
                    category: "jackets",
                    description:
                        "Waterproof 3-layer recycled nylon shell with fully sealed seams and printed logo tricot backing. Full zip closure with on seam zip hand pockets. Zip pockets at front and chest. Zip stash pocket at sleeve with interior microfiber goggle wipe. Interior elastic mesh pocket and two-way pit zips. Interior elastic shockcord at fixed hood and hem with velcro tab adjusters at cuffs.  Transparent watch window at cuff. Embroidered logos at chest, hood and back. Logo patches on sleeve. Made exclusively for Supreme.",
                    color: "Grey",
                    available: false,
                    sizes: [],
                },
                {
                    title: "Layered Hooded L/S Top",
                    price: "\u20ac98",
                    image: "https://assets.supremenewyork.com/245801/ma/57bBeGi29WQ.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/rpb0odr4m/yo6gyswqz?alt=0",
                    category: "tops-sweaters",
                    description: "All cotton jersey with printed logos on sleeves.",
                    color: "White",
                    available: true,
                    sizes: ["Large", "XLarge", "XXL"],
                },
                {
                    title: "Supreme\u00ae/The North Face\u00ae ",
                    price: "\u20ac438",
                    image: "https://assets.supremenewyork.com/250913/ma/PJYNnPAgL0I.jpg",
                    link: "https://www.supremenewyork.com/shop/jackets/mqg8xwafz/mivmpb64k?alt=2",
                    category: "jackets",
                    description:
                        "Waterproof 3-layer recycled nylon shell with fully sealed seams and printed logo tricot backing. Full zip closure with on seam zip hand pockets. Zip pockets at front and chest. Zip stash pocket at sleeve with interior microfiber goggle wipe. Interior elastic mesh pocket and two-way pit zips. Interior elastic shockcord at fixed hood and hem with velcro tab adjusters at cuffs.  Transparent watch window at cuff. Embroidered logos at chest, hood and back. Logo patches on sleeve. Made exclusively for Supreme.",
                    color: "Grey",
                    available: false,
                    sizes: [],
                },
                {
                    title: "Layered Hooded L/S Top",
                    price: "\u20ac98",
                    image: "https://assets.supremenewyork.com/245795/ma/0RSd-7h9zyM.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/rpb0odr4m/kjl3hfaki?alt=0",
                    category: "tops-sweaters",
                    description: "All cotton jersey with printed logos on sleeves.",
                    color: "Red",
                    available: true,
                    sizes: ["Large"],
                },
                {
                    title: "Layered Hooded L/S Top",
                    price: "\u20ac98",
                    image: "https://assets.supremenewyork.com/245799/ma/TTeOd3Tkr2o.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/rpb0odr4m/b86qo1ch5?alt=0",
                    category: "tops-sweaters",
                    description: "All cotton jersey with printed logos on sleeves.",
                    color: "Olive",
                    available: true,
                    sizes: ["Medium", "Large"],
                },
                {
                    title: "Supreme\u00ae/The North Face\u00ae",
                    price: "\u20ac238",
                    image: "https://assets.supremenewyork.com/250971/ma/Pa6ZNzcasZw.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/xrqg60y8x/j9zrxhtin?alt=0",
                    category: "tops-sweaters",
                    description:
                        "Merino wool with knit logo pattern. Full zip closure and pouch pocket at lower front. Made exclusively for Supreme.",
                    color: "Black",
                    available: true,
                    sizes: ["Large"],
                },
                {
                    title: "Layered Hooded L/S Top",
                    price: "\u20ac98",
                    image: "https://assets.supremenewyork.com/245797/ma/RwAi9M6rShU.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/rpb0odr4m/g5uspqow4?alt=0",
                    category: "tops-sweaters",
                    description: "All cotton jersey with printed logos on sleeves.",
                    color: "Black",
                    available: true,
                    sizes: ["Medium", "Large", "XLarge", "XXL"],
                },
                {
                    title: "Supreme\u00ae/The North Face\u00ae",
                    price: "\u20ac238",
                    image: "https://assets.supremenewyork.com/250975/ma/lKmFSbvH9PE.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/xrqg60y8x/jw6qh275y?alt=0",
                    category: "tops-sweaters",
                    description:
                        "Merino wool with knit logo pattern. Full zip closure and pouch pocket at lower front. Made exclusively for Supreme.",
                    color: "Pink",
                    available: false,
                    sizes: [],
                },
                {
                    title: "Supreme\u00ae/Nike\u00ae Air Force 1 Low",
                    price: "\u20ac128",
                    image: "https://assets.supremenewyork.com/247998/ma/aqXotkxJaFk.jpg",
                    link: "https://www.supremenewyork.com/shop/shoes/gxq0eu6dg/n3lsuwvz8?alt=2",
                    category: "shoes",
                    description:
                        "Full-grain leather upper with perforated leather toe panel and DURAPLUSH lining. Co-branded footbed, lace lock and tongue label. Embroidered logos at eyestay and heel with debossed printed logo at side. Set of printed logo laces included. Made exclusively for Supreme. ",
                    color: "Black",
                    available: true,
                    sizes: [
                        "US 8 / UK 7",
                        "US 8.5 / UK 7.5",
                        "US 9 / UK 8",
                        "US 9.5 / UK 8.5",
                        "US 10 / UK 9",
                        "US 10.5 / UK 9.5",
                        "US 11 / UK 10",
                    ],
                },
                {
                    title: "Supreme\u00ae/Nike\u00ae Air Force 1 Low",
                    price: "\u20ac150",
                    image: "https://assets.supremenewyork.com/248918/ma/Qqb2_7WGYoI.jpg",
                    link: "https://www.supremenewyork.com/shop/shoes/guarx76nw/twlsgaybj?alt=2",
                    category: "shoes",
                    description:
                        "Full-grain Nubuck upper with perforated leather toe panel and DURAPLUSH lining. Co-branded footbed, lace lock and tongue label. Embroidered logos at eyestay and heel with debossed printed logo at side. Set of printed logo laces included. Made exclusively for Supreme.",
                    color: "Wheat",
                    available: true,
                    sizes: [
                        "US 8 / UK 7",
                        "US 8.5 / UK 7.5",
                        "US 9 / UK 8",
                        "US 9.5 / UK 8.5",
                        "US 10 / UK 9",
                        "US 10.5 / UK 9.5",
                        "US 11 / UK 10",
                        "US 11.5 / UK 10.5",
                        "US 12 / UK 11",
                        "US 13 / UK 12",
                    ],
                },
                {
                    title: "Supreme\u00ae/The North Face\u00ae",
                    price: "\u20ac238",
                    image: "https://assets.supremenewyork.com/250973/ma/lpUJFLYi1VY.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/xrqg60y8x/jwbdljfoc?alt=0",
                    category: "tops-sweaters",
                    description:
                        "Merino wool with knit logo pattern. Full zip closure and pouch pocket at lower front. Made exclusively for Supreme.",
                    color: "Olive",
                    available: true,
                    sizes: ["Small", "Medium", "Large"],
                },
                {
                    title: "Supreme\u00ae/Nike\u00ae Air Force 1 Low",
                    price: "\u20ac150",
                    image: "https://assets.supremenewyork.com/248918/ma/Qqb2_7WGYoI.jpg",
                    link: "https://www.supremenewyork.com/shop/shoes/guarx76nw/twlsgaybj?alt=1",
                    category: "shoes",
                    description:
                        "Full-grain Nubuck upper with perforated leather toe panel and DURAPLUSH lining. Co-branded footbed, lace lock and tongue label. Embroidered logos at eyestay and heel with debossed printed logo at side. Set of printed logo laces included. Made exclusively for Supreme.",
                    color: "Wheat",
                    available: true,
                    sizes: [
                        "US 8 / UK 7",
                        "US 8.5 / UK 7.5",
                        "US 9 / UK 8",
                        "US 9.5 / UK 8.5",
                        "US 10 / UK 9",
                        "US 10.5 / UK 9.5",
                        "US 11 / UK 10",
                        "US 11.5 / UK 10.5",
                        "US 12 / UK 11",
                        "US 13 / UK 12",
                    ],
                },
                {
                    title: "Supreme\u00ae/Nike\u00ae Air Force 1 Low",
                    price: "\u20ac128",
                    image: "https://assets.supremenewyork.com/247998/ma/aqXotkxJaFk.jpg",
                    link: "https://www.supremenewyork.com/shop/shoes/gxq0eu6dg/n3lsuwvz8?alt=0",
                    category: "shoes",
                    description:
                        "Full-grain leather upper with perforated leather toe panel and DURAPLUSH lining. Co-branded footbed, lace lock and tongue label. Embroidered logos at eyestay and heel with debossed printed logo at side. Set of printed logo laces included. Made exclusively for Supreme. ",
                    color: "Black",
                    available: true,
                    sizes: [
                        "US 8 / UK 7",
                        "US 8.5 / UK 7.5",
                        "US 9 / UK 8",
                        "US 9.5 / UK 8.5",
                        "US 10 / UK 9",
                        "US 10.5 / UK 9.5",
                        "US 11 / UK 10",
                    ],
                },
                {
                    title: "Supreme\u00ae/Nike\u00ae Air Force 1 Low",
                    price: "\u20ac128",
                    image: "https://assets.supremenewyork.com/247998/ma/aqXotkxJaFk.jpg",
                    link: "https://www.supremenewyork.com/shop/shoes/gxq0eu6dg/n3lsuwvz8?alt=1",
                    category: "shoes",
                    description:
                        "Full-grain leather upper with perforated leather toe panel and DURAPLUSH lining. Co-branded footbed, lace lock and tongue label. Embroidered logos at eyestay and heel with debossed printed logo at side. Set of printed logo laces included. Made exclusively for Supreme. ",
                    color: "Black",
                    available: true,
                    sizes: [
                        "US 8 / UK 7",
                        "US 8.5 / UK 7.5",
                        "US 9 / UK 8",
                        "US 9.5 / UK 8.5",
                        "US 10 / UK 9",
                        "US 10.5 / UK 9.5",
                        "US 11 / UK 10",
                    ],
                },
                {
                    title: "Supreme\u00ae/Nike\u00ae Air Force 1 Low",
                    price: "\u20ac150",
                    image: "https://assets.supremenewyork.com/248918/ma/Qqb2_7WGYoI.jpg",
                    link: "https://www.supremenewyork.com/shop/shoes/guarx76nw/twlsgaybj?alt=0",
                    category: "shoes",
                    description:
                        "Full-grain Nubuck upper with perforated leather toe panel and DURAPLUSH lining. Co-branded footbed, lace lock and tongue label. Embroidered logos at eyestay and heel with debossed printed logo at side. Set of printed logo laces included. Made exclusively for Supreme.",
                    color: "Wheat",
                    available: true,
                    sizes: [
                        "US 8 / UK 7",
                        "US 8.5 / UK 7.5",
                        "US 9 / UK 8",
                        "US 9.5 / UK 8.5",
                        "US 10 / UK 9",
                        "US 10.5 / UK 9.5",
                        "US 11 / UK 10",
                        "US 11.5 / UK 10.5",
                        "US 12 / UK 11",
                        "US 13 / UK 12",
                    ],
                },
                {
                    title: "Bones S/S Top",
                    price: "\u20ac78",
                    image: "https://assets.supremenewyork.com/250373/ma/TjzzEFho4Nk.jpg",
                    link: "https://www.supremenewyork.com/shop/tops-sweaters/w6unm89ti/yipocgyrf?alt=0",
                    category: "tops-sweaters",
                    description:
                        "All cotton slub jersey crewneck with twill logo appliqu\u00e9 at chest. Athletic label at lower front.",
                    color: "Dark Royal",
                    available: true,
                    sizes: ["XLarge"],
                },
            ],
            finalList: [],
        };
    },
    beforeCreate() {
        //TODO: fetching data
    },
    beforeMount() {
        let perGroup = 4;
        let numGroups = Math.floor(this.itemList.length / perGroup) + 1;
        console.log(numGroups);
        this.finalList = new Array(numGroups)
            .fill("")
            .map((_, i) => this.itemList.slice(i * perGroup, (i + 1) * perGroup));
    },
    methods: {
        loadImg: function (url) {

        }
    },
};
</script>

<style scoped>

@import "@coreui/coreui/dist/css/coreui.min.css";
/**
     * style for the row container
     */

/**
     * style for the row
     */

.centered {
    display: flex;
    justify-content: center;
    align-items: center;
}

.row {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-around;
    width: 100%;
    margin-bottom: 1rem;
}

.row > * {
    padding-right: 0;
    padding-left: 0;
}

.drip-card {
    width: 18vw;
    height: 30vh;
    max-height: 30vh;
    border-radius: 25px;
    border: #2c3e50 1px solid;

    display: grid;
    grid-template-areas:
        "image"
        "title"
        "descritpion"
        "button";
    grid-template-columns: 1fr;
    grid-template-rows: 4fr 2fr 2.5fr 1fr;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
}

.item-img {
    width: 60%;
    display: block;
    margin-left: auto;
    margin-right: auto;
}

.image-box {
    border-top-left-radius: 25px;
    border-top-right-radius: 25px;
    grid-area: image;
    border-top: 25px;
    height: 100%;
    width: 100%;
}

.title-box {
    grid-area: title;
    width: 100%;
}

.item-title {
    font-weight: bold;
    font-size: 1rem;
}

.desc-box {
    grid-area: descritpion;
    /*background: #2c3e50;*/
    height: 100%;
    overflow: scroll;
    width: 100%;
    max-height: 100%;
}

.item-desc {
    font-size: 0.8rem;
    height: 100%;
    max-height: 100%;
}

.item-button {
    height: 100%;
    width: 60%;
    max-height: 100%;
    grid-area: button;
    border-radius: 25px;
    font-size: 0.8rem;
}


</style>