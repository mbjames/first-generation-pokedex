import pokemon_images
import pokemon
import pokemon_directory
import webbrowser
import banner


def menu():
    banner.print_banner()

    print("\n Please select a pokedex number. (1 - 151)")
    print(" Type (d) for a pokemon directory.")
    print(" Type (q) to exit.")

    answer = input("\n > ")

    browser_input = "pd"

    def sub_menu():
        browser_view = "\n Type (pd) to view in browser."
        go_back = "\n Press any key to go back."

        print(browser_view)
        print(go_back)

    if answer == "d":
        pokemon_directory.listing()
        menu()

    elif answer == "q":
        exit()

    elif answer == "1":
        pokemon_images.bulbasaur_image()

        pokemon.bulbasaur.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/bulbasaur")
            menu()

        else:
            menu()

    elif answer == "2":
        pokemon_images.ivysaur_image()

        pokemon.ivysaur.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/ivysaur")
            menu()

        else:
            menu()

    elif answer == "3":
        pokemon_images.venusaur_image()

        pokemon.venusaur.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/venusaur")
            menu()

        else:
            menu()

    elif answer == "4":
        pokemon_images.charmander_image()

        pokemon.charmander.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/charmander")
            menu()

        else:
            menu()

    elif answer == "5":
        pokemon_images.charmeleon_image()

        pokemon.charmeleon.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/charmeleon")
            menu()

        else:
            menu()

    elif answer == "6":
        pokemon_images.charizard_image()

        pokemon.charizard.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/charizard")
            menu()

        else:
            menu()

    elif answer == "7":
        pokemon_images.squirtle_image()

        pokemon.squirtle.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/squirtle")
            menu()

        else:
            menu()

    elif answer == "8":
        pokemon_images.wartortle_image()

        pokemon.wartortle.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/wartortle")
            menu()

        else:
            menu()

    elif answer == "9":
        pokemon_images.blastoise_image()

        pokemon.blastoise.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/blastoise")
            menu()

        else:
            menu()

    elif answer == "10":
        pokemon_images.caterpie_image()

        pokemon.caterpie.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/caterpie")
            menu()

        else:
            menu()

    elif answer == "11":
        pokemon_images.metapod_image()

        pokemon.metapod.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/metapod")
            menu()

        else:
            menu()

    elif answer == "12":
        pokemon_images.butterfree_image()

        pokemon.butterfree.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/butterfree")
            menu()

        else:
            menu()

    elif answer == "13":
        pokemon_images.weedle_image()

        pokemon.weedle.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/weedle")
            menu()

        else:
            menu()

    elif answer == "14":
        pokemon_images.kakuna_image()

        pokemon.kakuna.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/kakuna")
            menu()

        else:
            menu()

    elif answer == "15":
        pokemon_images.beedrill_image()

        pokemon.beedrill.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/beedrill")
            menu()

        else:
            menu()

    elif answer == "16":
        pokemon_images.pidgey_image()

        pokemon.pidgey.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/pidgey")
            menu()

        else:
            menu()

    elif answer == "17":
        pokemon_images.pidgeotto_image()

        pokemon.pidgeotto.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/pidgeotto")
            menu()

        else:
            menu()

    elif answer == "18":
        pokemon_images.pidgeot_image()

        pokemon.pidgeot.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/pidgeot")
            menu()

        else:
            menu()

    elif answer == "19":
        pokemon_images.rattata_image()

        pokemon.rattata.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/rattata")
            menu()

        else:
            menu()

    elif answer == "20":
        pokemon_images.raticate_image()

        pokemon.raticate.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/raticate")
            menu()

        else:
            menu()

    elif answer == "21":
        pokemon_images.spearow_image()

        pokemon.spearow.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/spearow")
            menu()

        else:
            menu()

    elif answer == "22":
        pokemon_images.fearow_image()

        pokemon.fearow.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/fearow")
            menu()

        else:
            menu()

    elif answer == "23":
        pokemon_images.ekans_image()

        pokemon.ekans.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/ekans")
            menu()

        else:
            menu()

    elif answer == "24":
        pokemon_images.arbok_image()

        pokemon.arbok.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/arbok")
            menu()

        else:
            menu()

    elif answer == "25":
        pokemon_images.pikachu_image()

        pokemon.pikachu.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/pikachu")
            menu()

        else:
            menu()

    elif answer == "26":
        pokemon_images.raichu_image()

        pokemon.raichu.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/raichu")
            menu()

        else:
            menu()

    elif answer == "27":
        pokemon_images.sandshrew_image()

        pokemon.sandshrew.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/sandshrew")
            menu()

        else:
            menu()

    elif answer == "28":
        pokemon_images.sandslash_image()

        pokemon.sandslash.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/sandslash")
            menu()

        else:
            menu()

    elif answer == "29":
        pokemon_images.nidoran_female_image()

        pokemon.nidoran_female.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/nidoran-f")
            menu()

        else:
            menu()

    elif answer == "30":
        pokemon_images.nidorina_image()

        pokemon.nidorina.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/nidorina")
            menu()

        else:
            menu()

    elif answer == "31":
        pokemon_images.nidoqueen_image()

        pokemon.nidoqueen.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/nidoqueen")
            menu()

        else:
            menu()

    elif answer == "32":
        pokemon_images.nidoran_male_image()

        pokemon.nidoran_male.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/nidoran-m")
            menu()

        else:
            menu()

    elif answer == "33":
        pokemon_images.nidorino_image()

        pokemon.nidorino.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/nidorino")
            menu()

        else:
            menu()

    elif answer == "34":
        pokemon_images.nidoking_image()

        pokemon.nidoking.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/nidoking")
            menu()

        else:
            menu()

    elif answer == "35":
        pokemon_images.clefairy_image()

        pokemon.clefairy.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/clefairy")
            menu()

        else:
            menu()

    elif answer == "36":
        pokemon_images.clefable_image()

        pokemon.clefable.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/clefable")
            menu()

        else:
            menu()

    elif answer == "37":
        pokemon_images.vulpix_image()

        pokemon.vulpix.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/vulpix")
            menu()

        else:
            menu()

    elif answer == "38":
        pokemon_images.ninetales_image()

        pokemon.ninetales.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/ninetales")
            menu()

        else:
            menu()

    elif answer == "39":
        pokemon_images.jigglypuff_image()

        pokemon.jigglypuff.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/jigglypuff")
            menu()

        else:
            menu()

    elif answer == "40":
        pokemon_images.wigglytuff_image()

        pokemon.wigglytuff.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/wigglytuff")
            menu()

        else:
            menu()

    elif answer == "41":
        pokemon_images.zubat_image()

        pokemon.zubat.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/zubat")
            menu()

        else:
            menu()

    elif answer == "42":
        pokemon_images.golbat_image()

        pokemon.golbat.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/golbat")
            menu()

        else:
            menu()

    elif answer == "43":
        pokemon_images.oddish_image()

        pokemon.oddish.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/oddish")
            menu()

        else:
            menu()

    elif answer == "44":
        pokemon_images.gloom_image()

        pokemon.gloom.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/gloom")
            menu()

        else:
            menu()

    elif answer == "45":
        pokemon_images.vileplume_image()

        pokemon.vileplume.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/vileplume")
            menu()

        else:
            menu()

    elif answer == "46":
        pokemon_images.paras_image()

        pokemon.paras.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/paras")
            menu()

        else:
            menu()

    elif answer == "47":
        pokemon_images.parasect_images()

        pokemon.parasect.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/parasect")
            menu()

        else:
            menu()

    elif answer == "48":
        pokemon_images.venonat_image()

        pokemon.venonat.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/venonat")
            menu()

        else:
            menu()

    elif answer == "49":
        pokemon_images.venomoth_image()

        pokemon.venomoth.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/venomoth")
            menu()

        else:
            menu()

    elif answer == "50":
        pokemon_images.diglett_image()

        pokemon.diglett.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/diglett")
            menu()

        else:
            menu()

    elif answer == "51":
        pokemon_images.dugtrio_image()

        pokemon.dugtrio.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/dugtrio")
            menu()

        else:
            menu()

    elif answer == "52":
        pokemon_images.meowth_image()

        pokemon.meowth.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/meowth")
            menu()

        else:
            menu()

    elif answer == "53":
        pokemon_images.persian_image()

        pokemon.persian.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/persian")
            menu()

        else:
            menu()

    elif answer == "54":
        pokemon_images.psyduck_image()

        pokemon.psyduck.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/psyduck")
            menu()

        else:
            menu()

    elif answer == "55":
        pokemon_images.golduck_image()

        pokemon.golduck.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/golduck")
            menu()

        else:
            menu()

    elif answer == "56":
        pokemon_images.mankey_image()

        pokemon.mankey.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/mankey")
            menu()

        else:
            menu()

    elif answer == "57":
        pokemon_images.primeape_image()

        pokemon.primeape.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/primeape")
            menu()

        else:
            menu()

    elif answer == "58":
        pokemon_images.growlithe_image()

        pokemon.growlithe.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/growlithe")
            menu()

        else:
            menu()

    elif answer == "59":
        pokemon_images.arcanine_image()

        pokemon.arcanine.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/arcanine")
            menu()

        else:
            menu()

    elif answer == "60":
        pokemon_images.poliwag_image()

        pokemon.poliwag.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/poliwag")
            menu()

        else:
            menu()

    elif answer == "61":
        pokemon_images.poliwhirl_image()

        pokemon.poliwhirl.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/poliwhirl")
            menu()

        else:
            menu()

    elif answer == "62":
        pokemon_images.poliwrath_image()

        pokemon.poliwrath.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/poliwrath")
            menu()

        else:
            menu()

    elif answer == "63":
        pokemon_images.abra_image()

        pokemon.abra.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/abra")
            menu()

        else:
            menu()

    elif answer == "64":
        pokemon_images.kadabra_image()

        pokemon.kadabra.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/kadabra")
            menu()

        else:
            menu()

    elif answer == "65":
        pokemon_images.alakazam_image()

        pokemon.alakazam.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/alakazam")
            menu()

        else:
            menu()

    elif answer == "66":
        pokemon_images.machop_image()

        pokemon.machop.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/machop")
            menu()

        else:
            menu()

    elif answer == "67":
        pokemon_images.machoke_image()

        pokemon.machoke.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/machoke")
            menu()

        else:
            menu()

    elif answer == "68":
        pokemon_images.machamp_image()

        pokemon.machamp.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/machamp")
            menu()

        else:
            menu()

    elif answer == "69":
        pokemon_images.bellsprout_image()

        pokemon.bellsprout.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/bellsprout")
            menu()

        else:
            menu()

    elif answer == "70":
        pokemon_images.weepinbell_image()

        pokemon.weepinbell.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/weepinbell")
            menu()

        else:
            menu()

    elif answer == "71":
        pokemon_images.victreebel_image()

        pokemon.victreebel.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/victreebel")
            menu()

        else:
            menu()

    elif answer == "72":
        pokemon_images.tentacool_image()

        pokemon.tentacool.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/tentacool")
            menu()

        else:
            menu()

    elif answer == "73":
        pokemon_images.tentacruel_image()

        pokemon.tentacruel.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/tentacruel")
            menu()

        else:
            menu()

    elif answer == "74":
        pokemon_images.geodude_image()

        pokemon.geodude.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/geodude")
            menu()

        else:
            menu()

    elif answer == "75":
        pokemon_images.graveler_image()

        pokemon.graveler.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/graveler")
            menu()

        else:
            menu()

    elif answer == "76":
        pokemon_images.golem_image()

        pokemon.golem.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/golem")
            menu()

        else:
            menu()

    elif answer == "77":
        pokemon_images.ponyta_image()

        pokemon.ponyta.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/ponyta")
            menu()

        else:
            menu()

    elif answer == "78":
        pokemon_images.rapidash_image()

        pokemon.rapidash.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/rapidash")
            menu()

        else:
            menu()

    elif answer == "79":
        pokemon_images.slowpoke_image()

        pokemon.slowpoke.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/slowpoke")
            menu()

        else:
            menu()

    elif answer == "80":
        pokemon_images.slowbro_image()

        pokemon.slowbro.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/slowbro")
            menu()

        else:
            menu()

    elif answer == "81":
        pokemon_images.magnemite_image()

        pokemon.magnemite.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/magnemite")
            menu()

        else:
            menu()

    elif answer == "82":
        pokemon_images.magneton_image()

        pokemon.magneton.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/magneton")
            menu()

        else:
            menu()

    elif answer == "83":
        pokemon_images.farfetchd_image()

        pokemon.farfetchd.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/farfetchd")
            menu()

        else:
            menu()

    elif answer == "84":
        pokemon_images.doduo_image()

        pokemon.doduo.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/doduo")
            menu()

        else:
            menu()

    elif answer == "85":
        pokemon_images.dodrio_image()

        pokemon.dodrio.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/dodrio")
            menu()

        else:
            menu()

    elif answer == "86":
        pokemon_images.seel_image()

        pokemon.seel.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/seel")
            menu()

        else:
            menu()

    elif answer == "87":
        pokemon_images.dewgong_image()

        pokemon.dewgong.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/dewgong")
            menu()

        else:
            menu()

    elif answer == "88":
        pokemon_images.grimer_image()

        pokemon.grimer.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/grimer")
            menu()

        else:
            menu()

    elif answer == "89":
        pokemon_images.muk_image()

        pokemon.muk.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/muk")
            menu()

        else:
            menu()

    elif answer == "90":
        pokemon_images.shellder_image()

        pokemon.shellder.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/shellder")
            menu()

        else:
            menu()

    elif answer == "91":
        pokemon_images.cloyster_image()

        pokemon.cloyster.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/cloyster")
            menu()

        else:
            menu()

    elif answer == "92":
        pokemon_images.gastly_image()

        pokemon.gastly.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/gastly")
            menu()

        else:
            menu()

    elif answer == "93":
        pokemon_images.haunter_image()

        pokemon.haunter.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/haunter")
            menu()

        else:
            menu()

    elif answer == "94":
        pokemon_images.gengar_image()

        pokemon.gengar.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/gengar")
            menu()

        else:
            menu()

    elif answer == "95":
        pokemon_images.onix_image()

        pokemon.onix.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/onix")
            menu()

        else:
            menu()

    elif answer == "96":
        pokemon_images.drowzee_image()

        pokemon.drowzee.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/drowzee")
            menu()

        else:
            menu()

    elif answer == "97":
        pokemon_images.hypno_image()

        pokemon.hypno.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/hypno")
            menu()

        else:
            menu()

    elif answer == "98":
        pokemon_images.krabby_image()

        pokemon.krabby.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/krabby")
            menu()

        else:
            menu()

    elif answer == "99":
        pokemon_images.kingler_image()

        pokemon.kingler.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/kingler")
            menu()

        else:
            menu()

    elif answer == "100":
        pokemon_images.voltorb_image()

        pokemon.voltorb.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/voltorb")
            menu()

        else:
            menu()

    elif answer == "101":
        pokemon_images.electrode_image()

        pokemon.electrode.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/electrode")
            menu()

        else:
            menu()

    elif answer == "102":
        pokemon_images.exeggcute_image()

        pokemon.exeggcute.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/exeggcute")
            menu()

        else:
            menu()

    elif answer == "103":
        pokemon_images.exeggutor_image()

        pokemon.exeggutor.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/exeggutor")
            menu()

        else:
            menu()

    elif answer == "104":
        pokemon_images.cubone_image()

        pokemon.cubone.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/cubone")
            menu()

        else:
            menu()

    elif answer == "105":
        pokemon_images.marowak_image()

        pokemon.marowak.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/marowak")
            menu()

        else:
            menu()

    elif answer == "106":
        pokemon_images.hitmonlee_image()

        pokemon.hitmonlee.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/hitmonlee")
            menu()

        else:
            menu()

    elif answer == "107":
        pokemon_images.hitmonchan_image()

        pokemon.hitmonchan.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/hitmonchan")
            menu()

        else:
            menu()

    elif answer == "108":
        pokemon_images.lickitung_image()

        pokemon.lickitung.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/lickitung")
            menu()

        else:
            menu()

    elif answer == "109":
        pokemon_images.koffing_image()

        pokemon.koffing.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/koffing")
            menu()

        else:
            menu()

    elif answer == "110":
        pokemon_images.weezing_image()

        pokemon.weezing.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/weezing")
            menu()

        else:
            menu()

    elif answer == "111":
        pokemon_images.rhyhorn_image()

        pokemon.rhyhorn.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/rhyhorn")
            menu()

        else:
            menu()

    elif answer == "112":
        pokemon_images.rhydon_image()

        pokemon.rhydon.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/rhydon")
            menu()

        else:
            menu()

    elif answer == "113":
        pokemon_images.chansey_image()

        pokemon.chansey.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/chansey")
            menu()

        else:
            menu()

    elif answer == "114":
        pokemon_images.tangela_image()

        pokemon.tangela.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/tangela")
            menu()

        else:
            menu()

    elif answer == "115":
        pokemon_images.kangaskhan_image()

        pokemon.kangaskhan.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/kangaskhan")
            menu()

        else:
            menu()

    elif answer == "116":
        pokemon_images.horsea_image()

        pokemon.horsea.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/horsea")
            menu()

        else:
            menu()

    elif answer == "117":
        pokemon_images.seadra_image()

        pokemon.seadra.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/seadra")
            menu()

        else:
            menu()

    elif answer == "118":
        pokemon_images.goldeen_image()

        pokemon.goldeen.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/goldeen")
            menu()

        else:
            menu()

    elif answer == "119":
        pokemon_images.seaking_image()

        pokemon.seaking.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/seaking")
            menu()

        else:
            menu()

    elif answer == "120":
        pokemon_images.staryu_image()

        pokemon.staryu.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/staryu")
            menu()

        else:
            menu()

    elif answer == "121":
        pokemon_images.starmie_image()

        pokemon.starmie.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/starmie")
            menu()

        else:
            menu()

    elif answer == "122":
        pokemon_images.mr_mime_image()

        pokemon.mr_mime.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/mr-mime")
            menu()

        else:
            menu()

    elif answer == "123":
        pokemon_images.scyther_image()

        pokemon.scyther.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/scyther")
            menu()

        else:
            menu()

    elif answer == "124":
        pokemon_images.jynx_image()

        pokemon.jynx.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/jynx")
            menu()

        else:
            menu()

    elif answer == "125":
        pokemon_images.electabuzz_image()

        pokemon.electabuzz.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/electabuzz")
            menu()

        else:
            menu()

    elif answer == "126":
        pokemon_images.magmar_image()

        pokemon.magmar.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/magmar")
            menu()

        else:
            menu()

    elif answer == "127":
        pokemon_images.pinsir_image()

        pokemon.pinsir.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/pinsir")
            menu()

        else:
            menu()

    elif answer == "128":
        pokemon_images.tauros_image()

        pokemon.tauros.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/tauros")
            menu()

        else:
            menu()

    elif answer == "129":
        pokemon_images.magikarp_image()

        pokemon.magikarp.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/magikarp")
            menu()

        else:
            menu()

    elif answer == "130":
        pokemon_images.gyarados_image()

        pokemon.gyarados.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/gyarados")
            menu()

        else:
            menu()

    elif answer == "131":
        pokemon_images.lapras_image()

        pokemon.lapras.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/lapras")
            menu()

        else:
            menu()

    elif answer == "132":
        pokemon_images.ditto_image()

        pokemon.ditto.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/ditto")
            menu()

        else:
            menu()

    elif answer == "133":
        pokemon_images.eevee_image()

        pokemon.eevee.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/eevee")
            menu()

        else:
            menu()

    elif answer == "134":
        pokemon_images.vaporeon_image()

        pokemon.vaporeon.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/vaporeon")
            menu()

        else:
            menu()

    elif answer == "135":
        pokemon_images.jolteon_image()

        pokemon.jolteon.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/jolteon")
            menu()

        else:
            menu()

    elif answer == "136":
        pokemon_images.flareon_image()

        pokemon.flareon.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/flareon")
            menu()

        else:
            menu()

    elif answer == "137":
        pokemon_images.porygon_image()

        pokemon.porygon.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/porygon")
            menu()

        else:
            menu()

    elif answer == "138":
        pokemon_images.omanyte_image()

        pokemon.omanyte.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/omanyte")
            menu()

        else:
            menu()

    elif answer == "139":
        pokemon_images.omastar_image()

        pokemon.omastar.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/omastar")
            menu()

        else:
            menu()

    elif answer == "140":
        pokemon_images.kabuto_image()

        pokemon.kabuto.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/kabuto")
            menu()

        else:
            menu()

    elif answer == "141":
        pokemon_images.kabutops_image()

        pokemon.kabutops.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/kabutops")
            menu()

        else:
            menu()

    elif answer == "142":
        pokemon_images.aerodactyl_image()

        pokemon.aerodactyl.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/aerodactyl")
            menu()

        else:
            menu()

    elif answer == "143":
        pokemon_images.snorlax_image()

        pokemon.snorlax.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/snorlax")
            menu()

        else:
            menu()

    elif answer == "144":
        pokemon_images.articuno_image()

        pokemon.articuno.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/articuno")
            menu()

        else:
            menu()

    elif answer == "145":
        pokemon_images.zapdos_image()

        pokemon.zapdos.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/zapdos")
            menu()

        else:
            menu()

    elif answer == "146":
        pokemon_images.moltres_image()

        pokemon.moltres.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/moltres")
            menu()

        else:
            menu()

    elif answer == "147":
        pokemon_images.dratini_image()

        pokemon.dratini.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/dratini")
            menu()

        else:
            menu()

    elif answer == "148":
        pokemon_images.dragonair_image()

        pokemon.dragonair.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/dragonair")
            menu()

        else:
            menu()

    elif answer == "149":
        pokemon_images.dragonite_image()

        pokemon.dragonite.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/dragonite")
            menu()

        else:
            menu()

    elif answer == "150":
        pokemon_images.mewtwo_image()

        pokemon.mewtwo.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/mewtwo")
            menu()

        else:
            menu()

    elif answer == "151":
        pokemon_images.mew_image()

        pokemon.mew.print()

        sub_menu()

        answer = input("\n > ")

        if answer == browser_input:
            webbrowser.open_new("https://pokemondb.net/pokedex/mew")
            menu()

        else:
            menu()

    else:
        menu()


menu()
