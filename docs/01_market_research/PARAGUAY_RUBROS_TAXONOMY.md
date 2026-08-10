# Paraguay Rubros Taxonomy — Directory → Builder Mapping

Reference document that maps the **Paraguayan business-directory rubro taxonomy** (18 optgroups, ~144 specific rubros) to the `paragu-ai-builder` registry. Use this as the lookup when qualifying a lead whose source listing reports a rubro ID/label — it tells you which builder vertical and `type.json` to use to spin up a site.

**Source format:** HTML `<select name="rubro_comercio_servicio">` from a Paraguayan SME directory (ClasiPar-style). Each option has a numeric `value` (directory-local ID) and a Spanish label. `solicitar_rubro="1"` on "Otros" entries means the directory asks the user to type a custom rubro.

**Builder registry:** `paragu-ai-builder/src/registry/` — v3.0.0, 1900+ business types across 23 verticals. Verticals catalog: `src/verticals/catalog.json`.

---

## 1. At a glance

| Metric | Value |
|---|---|
| Directory optgroups (top-level rubros) | 18 |
| Specific rubros (excl. "Otros") | 126 |
| "Otros" catch-alls | 18 |
| **Total directory options** | **144** |
| Rubros mappable to existing builder types | 126 (100% of specific rubros, after PR #85 + #88 closed all 17 gaps) |
| Rubros needing a new registry entry | 0 — all closed |
| Builder verticals covered by the directory | 18 of 23 |
| Builder verticals **not** reached by the directory | 5 (agriculture, death-care, hospitality-tourism full, membership-community, real-estate-relocation, arts-entertainment-venues partial) |

---

## 2. Optgroup → Builder vertical

Each directory optgroup maps to one primary builder vertical (sometimes two for mixed groups).

| Directory optgroup | Primary builder vertical | Secondary |
|---|---|---|
| Asesoramiento | `b2b-professional` | `finance-insurance` (Seguros) |
| Belleza y Cuidado Personal | `beauty-personal-care` | `service-booking` (Personal Trainer) |
| Comunicación y Diseño | `portfolio-professional` | `technology-digital` (Marketing) |
| Cursos y Clases | `education-training` | — |
| Delivery | `food-beverage` | `logistics-transport` |
| Fiestas y Eventos | `arts-entertainment-venues` | `food-beverage` (Catering/Bebidas) |
| Fotografía, Música y Cine | `portfolio-professional` | `arts-entertainment-venues` |
| Hogar y Construcción | `trades-home-services` | — |
| Imprenta | `b2b-professional` | `retail-local` |
| Mantenimiento de Vehículos | `automotive` | — |
| Medicina y Salud | `health-wellness` | — |
| Ropa y Moda | `retail-local` | `trades-home-services` (Lavandería) |
| Mascotas | `pets-animals` | — |
| Oficinas | `b2b-professional` | `retail-local` |
| Tecnología | `technology-digital` | `retail-local` |
| Transporte | `logistics-transport` | — |
| Viajes y Turismo | `hospitality-tourism` | — |

---

## 3. Full rubro table

Columns:
- **Dir ID** — the directory's numeric `value`
- **Rubro (ES)** — directory label
- **Builder vertical** — target vertical slug
- **Builder type** — best-fit `type.json` from `src/registry/`. Multiple slugs = pick by business specifics.
- **Status** — ✅ registered · ⚠ use closest · 🆕 gap (no direct match)

### 3.1 Asesoramiento → `b2b-professional` + `finance-insurance`

| Dir ID | Rubro | Builder vertical | Builder type | Status |
|---|---|---|---|---|
| 20 | Abogados y Estudios Jurídicos | b2b-professional | `corporate_business_lawyer`, `family_divorce_lawyer`, `criminal_defense_lawyer`, `immigration_lawyer`, `employment_lawyer`, `intellectual_property_lawyer`, `general_practice_lawyer`, `estate_probate_lawyer` | ✅ (sub-specialty split) |
| 21 | Contadores y Estudios | b2b-professional | `contador`, `cpa_firm`, `auditoria`, `bookkeeper`, `forensic_accountant` | ✅ |
| 22 | Despachantes de Aduana | b2b-professional | `despachante`, `agencia_aduana`, `customs_broker` | ✅ |
| 23 | Gestores | b2b-professional | `consultoria` (generic), `errand_runner` | ⚠ use closest |
| 24 | Seguros | finance-insurance | `auto_insurance_agency`, `health_insurance_broker`, `home_insurance_agency`, `commercial_insurance_broker`, `independent_insurance_agent`, `broker_seguros` | ✅ |
| 25 | Tasadores | b2b-professional | `commercial_appraiser` | ✅ |
| 26 | Otros | b2b-professional | — | ⚠ custom |

### 3.2 Belleza y Cuidado Personal → `beauty-personal-care`

> Highest-priority vertical: **3,960 Priority A leads** from the CSV scrape live here. Content/tokens already extracted per `BUILDER_EXTRACTION_MAP.md`.

| Dir ID | Rubro | Builder vertical | Builder type | Status |
|---|---|---|---|---|
| 28 | Cosmetología | beauty-personal-care | `cosmetology_school`, `esthetician_solo`, `facial_spa` | ✅ |
| 29 | Cuidado Personal | beauty-personal-care | `beauty_base`, `centro_integral_belleza` | ✅ |
| 30 | Depilación | beauty-personal-care | `depilacion`, `brazilian_wax_studio`, `ipl_hair_removal`, `electrolysis_clinic` | ✅ |
| 31 | Estética | beauty-personal-care | `estetica`, `cirugia_estetica`, `cosmetic_surgery_practice`, `botox_filler_clinic`, `hydrafacial_studio` | ✅ |
| 32 | Manicuría y Pedicuría | beauty-personal-care | `unas`, `gel_acrylic_nail_studio`, `dip_powder_nail_studio` | ✅ |
| 33 | Maquilladoras y Peinadoras | beauty-personal-care | `bridal_makeup_artist`, `airbrush_makeup_studio`, `bridal_hair_specialist` | ✅ |
| 34 | Masajes y Tratamientos | beauty-personal-care / health-wellness | `day_spa`, `aromatherapy_studio`, `hammam_turkish_bath`, `cupping_therapy_studio`, `float_tank_center` | ✅ |
| 35 | Peluquería | beauty-personal-care | `peluqueria`, `hair_salon`, `hair_color_studio`, `blow_dry_bar`, `braiding_salon`, `afro_textured_salon`, `alisado_capilar`, `extensiones_cabello` | ✅ **pilot target** |
| 36 | Personal Trainer | service-booking | `personal_trainer` (verify), `functional_training_studio`, `crossfit_box` | ⚠ verify slug |
| 37 | Tatuajes y Piercings | beauty-personal-care | `tatuajes` (verify), `body_piercing_studio`, `cosmetic_tattoo_studio`, `henna_tattoo_studio` | ⚠ verify slug |
| 38 | Otros | beauty-personal-care | — | ⚠ custom |

### 3.3 Comunicación y Diseño → `portfolio-professional` + `technology-digital`

| Dir ID | Rubro | Builder vertical | Builder type | Status |
|---|---|---|---|---|
| 40 | Diseñadores Gráficos | portfolio-professional | `diseno_grafico`, `graphic_design_studio`, `illustrator_studio`, `branding_agency` | ✅ |
| 41 | Locutores | portfolio-professional | `voice_over_studio`, `audiobook_narrator` | ✅ |
| 42 | Marketing y Publicidad | technology-digital | `full_service_marketing_agency`, `content_marketing_agency`, `email_marketing_agency`, `direct_mail_agency`, `influencer_marketing_agency`, `experiential_marketing_agency`, `instagram_tiktok_agency` | ✅ |
| 43 | Traductores | b2b-professional | `certified_translator`, `court_legal_interpreter` | ✅ |
| 44 | Otros | portfolio-professional | — | ⚠ custom |

### 3.4 Cursos y Clases → `education-training`

| Dir ID | Rubro | Builder vertical | Builder type | Status |
|---|---|---|---|---|
| 46 | Apoyo Escolar y Universitario | education-training | `apoyo_escolar`, `in_person_tutoring_center`, `english_tutor`, `homework_help_service` | ✅ |
| 47 | Artes Plásticas | education-training | `art_studio_classes`, `ceramicist_pottery_studio`, `art_supply_store` | ✅ |
| 48 | Canto y Baile | education-training | `ballet_school`, `dance_studio_classes`, `hip_hop_dance_studio`, `drum_percussion_studio`, `escuela_musica` | ✅ |
| 49 | Cocina | education-training | `academia_cocina`, `culinary_school`, `bartending_school` | ✅ |
| 50 | Computación e Informática | education-training | `coding_bootcamp`, `devops_cloud_bootcamp`, `cybersecurity_bootcamp`, `data_science_bootcamp`, `ai_ml_bootcamp` | ✅ |
| 51 | Conducción | education-training | `escuela_conducir`, `general_driving_school`, `defensive_driving_course` | ✅ |
| 52 | Contabilidad y Economía | education-training | `cpa_exam_prep`, `centro_capacitacion` (generic) | ⚠ closest |
| 53 | Deportes | sports-recreation / education-training | `baseball_softball_academy`, `basketball_academy`, `hockey_academy`, `esports_training_academy`, `golf_pro` | ✅ |
| 54 | Fotografía | education-training | `photography_academy` | ✅ |
| 55 | Idiomas | education-training | `academia_idiomas`, `academia_portugues`, `english_academy`, `esl_center`, `instituto_ingles` | ✅ |
| 56 | Instrumentos Musicales | education-training | `guitar_lessons`, `escuela_musica`, `drum_percussion_studio` | ✅ |
| 57 | Marketing Digital | education-training | `digital_marketing_academy` | ✅ |
| 58 | Maquillaje (clases) | education-training | `cosmetology_school` (overlap) | ⚠ closest |
| 59 | Mecánica (clases) | education-training | `mechanics_trade_school`, `hvac_trade_school`, `electrician_apprentice_school` | ✅ |
| 60 | Tatuajes (clases) | education-training | `tattoo_academy` | ✅ |
| 61 | Tecnología | education-training | `coding_bootcamp` et al. (same as 50) | ✅ |
| 62 | Otros | education-training | — | ⚠ custom |

### 3.5 Delivery → `food-beverage`

| Dir ID | Rubro | Builder vertical | Builder type | Status |
|---|---|---|---|---|
| 64 | Desayunos | food-beverage | `diet_meal_delivery`, `drop_off_caterer`, `frozen_meal_brand` | ⚠ closest |
| 65 | Viandas | food-beverage | `diet_meal_delivery` (**De Abasto a Casa** lives here) | ✅ |
| 66 | Otros | food-beverage | — | ⚠ custom |

### 3.6 Fiestas y Eventos → `arts-entertainment-venues` + `food-beverage`

| Dir ID | Rubro | Builder vertical | Builder type | Status |
|---|---|---|---|---|
| 68 | Alquiler de Carpas y Tiendas | arts-entertainment-venues | `event_equipment_rental` | ✅ |
| 69 | Alquiler de Equipos | arts-entertainment-venues | `event_equipment_rental` | ✅ |
| 70 | Alquiler de Escenarios | arts-entertainment-venues | `event_equipment_rental` | ✅ |
| 71 | Alquiler de Indumentaria | arts-entertainment-venues | `formalwear_rental`, `costume_designer` | ✅ |
| 72 | Alquiler de Mobiliario | arts-entertainment-venues | `event_equipment_rental` | ✅ |
| 73 | Animación y Alquiler de juegos | arts-entertainment-venues | `bouncy_castle_rental`, `childrens_entertainer`, `clown_entertainer`, `balloon_artist`, `face_painter` | ✅ |
| 74 | Bebidas | food-beverage | `bartending_service` | ✅ |
| 75 | Catering | food-beverage | `catering`, `full_service_caterer`, `corporate_caterer`, `drop_off_caterer`, `bbq_catering`, `halal_caterer`, `hog_roast_service` | ✅ |
| 76 | Decoración y Ambientación | arts-entertainment-venues | `decoracion_hogar`, `home_staging_designer`, `ice_sculpture_artist` | ⚠ closest |
| 77 | Personal Gastronómico | food-beverage | `event_staffing_hospitality` | ✅ |
| 78 | Salones | arts-entertainment-venues | `banquet_hall`, `beach_event_venue`, `barn_rustic_venue`, `estancia_event_venue`, `church_chapel_venue` | ✅ |
| 79 | Servicios Audiovisuales | portfolio-professional / arts-entertainment-venues | `audio_post_production`, `commercial_video_production`, `drone_videography`, `av_integrator_residential`, `av_integrator_commercial`, `dj_service` | ✅ |
| 80 | Vehículos para Eventos | arts-entertainment-venues | `glam_bus_party_service`, `charter_bus_service` | ✅ |
| 81 | Otros | arts-entertainment-venues | — | ⚠ custom |

### 3.7 Fotografía, Música y Cine → `portfolio-professional` + `arts-entertainment-venues`

| Dir ID | Rubro | Builder vertical | Builder type | Status |
|---|---|---|---|---|
| 83 | Cine y Televisión | arts-entertainment-venues / portfolio-professional | `documentary_filmmaker`, `film_festival_producer`, `film_scoring_composer`, `animation_studio`, `drive_in_theater`, `independent_cinema`, `imax_premium_theater` | ✅ |
| 84 | Fotografía | portfolio-professional | `fotografia_bodas`, `fotografia_eventos`, `fotografia_producto`, `event_photographer`, `family_photographer`, `headshot_photographer`, `boudoir_photographer`, `commercial_product_photographer`, `drone_aerial_photographer` | ✅ |
| 85 | Música | arts-entertainment-venues | `concert_hall`, `electronic_music_club`, `blues_club`, `dance_club`, `escuela_musica`, `film_scoring_composer` | ✅ |
| 86 | Otros | portfolio-professional | — | ⚠ custom |

### 3.8 Hogar y Construcción → `trades-home-services`

| Dir ID | Rubro | Builder vertical | Builder type | Status |
|---|---|---|---|---|
| 88 | Instalación y Servicio Técnico | trades-home-services | `appliance_installer`, `appliance_repair`, `alarm_security_installer`, `access_control_installer`, `ev_charger_installer`, `home_automation_security`, `home_theater_installer`, `hot_tub_installer`, `gate_installer` | ✅ |
| 89 | Mantenimiento del Hogar | trades-home-services | `handyman_service`, `house_cleaning_service`, `deep_cleaning_service`, `eco_green_cleaning`, `drain_cleaning_service`, `gutter_installation`, `chimney_sweep`, `destapaciones`, `fumigacion`, `electricista`, `general_plumber`, `emergency_plumber`, `emergency_electrician`, `cerrajero`, `carpintero`, `albanil`, `herreria`, `aire_acondicionado` | ✅ |
| 90 | Obras y Construcción | trades-home-services | `general_contractor`, `custom_home_builder`, `commercial_developer`, `commercial_electrician`, `commercial_hvac`, `basement_finishing`, `bathroom_remodeler`, `home_addition_builder`, `home_remodeler`, `deck_builder`, `commercial_roofer`, `flat_roof_specialist`, `drywall_contractor`, `framing_contractor`, `hardscape_paver_installer`, `concrete_aggregate_supplier` | ✅ |
| 91 | Otros | trades-home-services | — | ⚠ custom |

### 3.9 Imprenta → `b2b-professional` + `retail-local`

| Dir ID | Rubro | Builder vertical | Builder type | Status |
|---|---|---|---|---|
| 93 | Folletería y Catálogos | b2b-professional | `commercial_print_shop`, `digital_print_shop` | ✅ |
| 94 | Impresiones en Gran Formato | b2b-professional | `banner_tradeshow_graphics`, `commercial_signage_digital` | ✅ |
| 95 | Impresiones Láser | b2b-professional | `digital_print_shop`, `dtf_dtg_garment_printer` | ✅ |
| 96 | Otros | b2b-professional | — | ⚠ custom |

### 3.10 Mantenimiento de Vehículos → `automotive`

| Dir ID | Rubro | Builder vertical | Builder type | Status |
|---|---|---|---|---|
| 98 | Audio | automotive | `car_audio_shop` | ✅ |
| 99 | Cerrajería | automotive | `automotive_locksmith` | ✅ |
| 100 | Cuidado del Vehículo | automotive | `auto_detailing_shop`, `detailing`, `hand_car_wash`, `automatic_car_wash`, `ceramic_coating_studio`, `interior_detailing_specialist`, `engine_bay_detailing` | ✅ |
| 101 | Diagnósticos | automotive | `auto_electrical_shop`, `ecu_tuning_specialist`, `dyno_tuning_shop` | ✅ |
| 102 | Llantas y Neumáticos | automotive | `gomeria`, `alineacion_balanceo`, `custom_wheel_shop` | ✅ |
| 103 | Lubricentros | automotive | `lubricentro`, `general_auto_repair` | ✅ |
| 104 | Náutica | automotive / hospitality-tourism | `boat_repair_marina` | ✅ |
| 105 | Parabrisas y Cristales | automotive | `glass_windshield_repair` | ✅ |
| 106 | Seguridad Vehicular | automotive | `auto_insurance_agency`, `cctv_camaras` (for vehicles) | ⚠ closest |
| 107 | Talleres | automotive | `general_auto_repair`, `collision_repair_center`, `auto_body_shop`, `brake_specialist`, `exhaust_muffler_shop`, `engine_rebuild_shop`, `engine_swap_shop`, `diesel_repair_shop`, `hybrid_repair_specialist`, `ev_repair_specialist`, `frame_straightening`, `auto_ac_specialist` | ✅ |
| 108 | Tunning | automotive | `dyno_tuning_shop`, `ecu_tuning_specialist`, `custom_wheel_shop`, `car_audio_shop` | ✅ |
| 109 | Otros | automotive | — | ⚠ custom |

### 3.11 Medicina y Salud → `health-wellness`

| Dir ID | Rubro | Builder vertical | Builder type | Status |
|---|---|---|---|---|
| 111 | Estudios Varios | health-wellness | `centro_diagnostico`, `imaging_center`, `clinical_laboratory`, `dna_genetic_testing`, `cardiology_diagnostics` | ✅ |
| 112 | Prepagas | finance-insurance | `prepaid_health_plan`, `health_insurance_broker` | ✅ |
| 113 | Profesionales | health-wellness | `family_medicine_clinic`, `internal_medicine_practice`, `dermatology_clinic`, `dermatologia`, `gynecology_clinic`, `ginecologia`, `geriatria`, `cardiology_clinic`, `gastroenterology_clinic`, `endocrinology_clinic`, `ent_clinic`, `fertility_clinic`, `general_dental_practice`, `consultorio_odontologico`, `chiropractic_clinic`, `acupuncture_clinic`, `fonoaudiologia`, `hand_therapy_clinic`, `homeopathy_practice`, `concierge_medicine` | ✅ |
| 114 | Servicios de Ambulancia | health-wellness | `ambulance_service` | ✅ |
| 115 | Servicios de Ortopedia | health-wellness | `orthopedic_supply`, `hearing_aid_store`, `denture_clinic` | ✅ |
| 116 | Otros | health-wellness | — | ⚠ custom |

### 3.12 Ropa y Moda → `retail-local` + `trades-home-services`

| Dir ID | Rubro | Builder vertical | Builder type | Status |
|---|---|---|---|---|
| 118 | Arreglos | retail-local | `bespoke_tailor` | ✅ |
| 119 | Bordados | retail-local | `embroidery_shop` | ✅ |
| 120 | Confección | retail-local | `apparel_manufacturer`, `cut_and_sew_shop`, `contract_manufacturer` | ✅ |
| 121 | Corte y Moldería | retail-local | `fashion_designer`, `cut_and_sew_shop` | ⚠ closest |
| 122 | Estampados | retail-local | `dtf_dtg_garment_printer`, `embroidery_shop` | ✅ |
| 123 | Lavandería y Tintorería | trades-home-services | `laundry_dry_cleaning` | ✅ |
| 124 | Otros | retail-local | — | ⚠ custom |

### 3.13 Mascotas → `pets-animals`

| Dir ID | Rubro | Builder vertical | Builder type | Status |
|---|---|---|---|---|
| 126 | Adiestramiento Canino | pets-animals | `dog_obedience_trainer`, `agility_dog_training`, `behavior_modification_trainer` | ✅ |
| 127 | Cruza | pets-animals | `dog_breeder`, `cat_breeder`, `horse_breeder`, `bird_breeder` | ✅ |
| 128 | Cuidado e Higiene | pets-animals | `dog_grooming_salon`, `cat_grooming_studio`, `breed_specific_grooming` | ✅ |
| 129 | Paseadores de Perros | pets-animals | `dog_walker` | ✅ |
| 130 | Peluquerías Caninas | pets-animals | `dog_grooming_salon` | ✅ |
| 131 | Pensionados y Guarderías | pets-animals | `dog_boarding_kennel`, `doggy_daycare`, `cat_boarding`, `exotic_pet_boarding`, `in_home_pet_sitter` | ✅ |
| 132 | Perros en Adopción | pets-animals | `humane_society_shelter`, `animal_rescue_nonprofit`, `breed_specific_rescue` | ✅ |
| 133 | Traslados | pets-animals | `pet_transport_service` | ✅ |
| 134 | Veterinaria | pets-animals | `general_veterinary_clinic`, `emergency_veterinary_hospital`, `equine_veterinary`, `exotic_pet_vet` | ✅ |
| 135 | Otros | pets-animals | — | ⚠ custom |

### 3.14 Oficinas → `b2b-professional` + `retail-local`

| Dir ID | Rubro | Builder vertical | Builder type | Status |
|---|---|---|---|---|
| 137 | Dispensers y Expendedoras | b2b-professional | `vending_water_dispenser_service`, `atm_operator`, `bill_pay_kiosk` | ✅ |
| 138 | Equipos de Fitness | retail-local | `fitness_equipment_dealer` | ✅ |
| 139 | Fotocopiadoras | b2b-professional | `copier_dealer_service`, `commercial_print_shop` | ✅ |
| 140 | Montacargas y Ascensores | trades-industrial | `forklift_dealer` | ✅ (partial) |
| 141 | Otros | b2b-professional | — | ⚠ custom |

### 3.15 Tecnología → `technology-digital` + `retail-local`

| Dir ID | Rubro | Builder vertical | Builder type | Status |
|---|---|---|---|---|
| 143 | Alarmas y Cámaras de Seguridad | trades-home-services | `alarm_security_installer`, `cctv_camera_installer`, `cctv_camaras` | ✅ |
| 144 | Audio y Video | retail-local | `audio_video_showroom`, `av_integrator_residential`, `av_integrator_commercial`, `home_theater_installer` | ✅ |
| 145 | Cámaras Digitales | retail-local | `camera_photo_shop` | ✅ |
| 146 | Celulares y Telefonía | retail-local | `celulares_accesorios`, `cell_phone_repair` | ✅ |
| 147 | Computación | retail-local | `computer_shop`, `computer_repair_shop`, `informatica_venta` | ✅ |
| 148 | Consolas | retail-local | `console_gaming_repair`, `game_store_board`, `esports_lounge` | ✅ |
| 149 | GPS | automotive / retail-local | `electronics_shop` (generic) | ⚠ closest |
| 150 | Hosting | technology-digital | `web_hosting_provider`, `data_warehouse_firm`, `cloud_migration_firm` | ✅ |
| 151 | Programadores | technology-digital | `desarrollo_software`, `desarrollo_software_empresa`, `ecommerce_development`, `diseno_web`, `chatbot_automation_studio`, `it_consulting` | ✅ |
| 152 | Relojes | retail-local | `watch_jeweler_shop`, `fine_jewelry_store` | ✅ |
| 153 | Otros | technology-digital | — | ⚠ custom |

### 3.16 Transporte → `logistics-transport`

| Dir ID | Rubro | Builder vertical | Builder type | Status |
|---|---|---|---|---|
| 155 | Alquiler de autos | logistics-transport / hospitality-tourism | `alquiler_vehiculos`, `car_rental_agency`, `car_subscription_service` | ✅ |
| 156 | Encomiendas y Mensajerías | logistics-transport | `bicycle_courier`, `document_legal_courier`, `express_air_courier` | ✅ |
| 157 | Mudanzas | logistics-transport | `international_household_mover`, `international_movers`, `art_antique_movers` | ✅ |
| 158 | Pasajeros | logistics-transport | `charter_bus_service`, `airport_shuttle_service` | ✅ |
| 159 | Remolques | logistics-transport / automotive | `grua_remolque`, `heavy_duty_towing`, `heavy_haul_oversize`, `flatbed_specialized_hauling` | ✅ |
| 160 | Otros | logistics-transport | — | ⚠ custom |

### 3.17 Viajes y Turismo → `hospitality-tourism`

| Dir ID | Rubro | Builder vertical | Builder type | Status |
|---|---|---|---|---|
| 162 | Alojamiento | hospitality-tourism | `hotel`, `hotel_boutique`, `boutique_hotel`, `hostal`, `backpacker_hostel`, `bed_and_breakfast`, `apart_hotel`, `airport_hotel`, `budget_hotel_chain`, `business_hotel`, `beach_resort`, `all_inclusive_resort`, `glamping_resort`, `eco_lodge`, `estancia_turistica`, `farm_stay`, `cabanas_turisticas`, `guesthouse`, `inn_lodge`, `alquiler_temporario`, `houseboat_rental`, `capsule_hotel`, `cabin_rental`, `cabin_campground` | ✅ (deep coverage) |
| 163 | Alquiler de Autos | hospitality-tourism | `alquiler_vehiculos`, `car_rental_agency` (same as 155) | ✅ |
| 164 | Asistencia al Viajero | hospitality-tourism | `destination_service_provider`, `expat_settling_in_service`, `event_wedding_insurance` | ✅ |
| 165 | Excursiones y Paseos | hospitality-tourism | `city_walking_tour`, `adventure_tour_operator`, `agritourism_farm`, `cultural_heritage_tour`, `food_tour_operator`, `ghost_haunted_tour`, `bike_tour_operator`, `boat_cruise_tour`, `balloon_ride_operator`, `helicopter_tour`, `fishing_charter`, `dive_charter`, `canyoning_guide`, `dog_sled_tour` | ✅ |
| 166 | Paquetes Turísticos | hospitality-tourism | `group_tour_packager`, `agencia_viajes`, `full_service_travel_agency`, `cruise_specialist`, `honeymoon_specialist` | ✅ |
| 167 | Pasajes | hospitality-tourism | `agencia_viajes`, `full_service_travel_agency`, `corporate_travel_management` | ✅ |
| 168 | Otros | hospitality-tourism | — | ⚠ custom |

---

## 4. Registry gaps — ✅ ALL CLOSED

All 17 gaps originally identified here were closed:
- **P1 (2):** merged to builder in [PR #85](https://github.com/Ai-Whisperers/paragu-ai-builder/pull/85) — `laundry_dry_cleaning`, `ambulance_service`
- **P2-P5 (15):** merged in [PR #88](https://github.com/Ai-Whisperers/paragu-ai-builder/pull/88) — `lubricentro`, `fitness_equipment_dealer`, `web_hosting_provider`, `event_equipment_rental`, `event_staffing_hospitality`, `pet_transport_service`, `copier_dealer_service`, `vending_water_dispenser_service`, `watch_jeweler_shop`, `orthopedic_supply`, `prepaid_health_plan`, `mechanics_trade_school`, `tattoo_academy`, `photography_academy`, `voice_over_studio`

The Paraguay rubro taxonomy now maps **100% to the builder registry**. §3 above reflects the current state.

### If a new gap is discovered later
Add a row to the relevant §3 subsection, mark the status as 🆕, and file a new registry entry in `paragu-ai-builder/src/registry/` using the minimal extends-from-base pattern (see `laundry_dry_cleaning.type.json` or `voice_over_studio.type.json` as templates).

---

## 5. Cross-reference: rubros vs. CSV lead data

The Google Maps scrape in `data/processed/paraguay_priority_a.csv` only covered the **9 beauty & wellness categories** (dir IDs 28–37). The remaining ~135 rubros in this directory are **unscraped market** — a future lead-extraction pass should widen the Google Places query to cover them.

Estimated scale by optgroup (rough, to prioritize the next scrape):

| Optgroup | Estimated Paraguay SME count | Already scraped? |
|---|---:|---|
| Belleza y Cuidado Personal | 7,463 | ✅ |
| Medicina y Salud | ~5,000–8,000 | ❌ |
| Hogar y Construcción | ~6,000–10,000 | ❌ |
| Mantenimiento de Vehículos | ~3,000–5,000 | ❌ |
| Viajes y Turismo | ~2,000–4,000 | ❌ |
| Cursos y Clases | ~3,000–5,000 | ❌ |
| Fiestas y Eventos | ~2,000–3,000 | ❌ |
| Transporte | ~2,000–4,000 | ❌ |
| Ropa y Moda | ~2,000–3,000 | ❌ |
| Mascotas | ~1,500–2,500 | ❌ |
| Asesoramiento | ~2,500–4,000 | ❌ |
| Tecnología | ~1,000–2,000 | ❌ |
| Delivery | ~500–1,500 | ❌ (De Abasto a Casa already a live tenant) |
| Comunicación y Diseño | ~1,000–2,000 | ❌ (Dayah Litworks already a live tenant) |
| Fotografía/Música/Cine | ~1,000–2,000 | ❌ |
| Imprenta | ~500–1,000 | ❌ |
| Oficinas | ~500–1,000 | ❌ |

---

## 6. How to use this document

### When qualifying a new lead
1. Identify the lead's rubro (directory ID or label).
2. Look up the row in §3. Note the **builder vertical** and primary **builder type**.
3. Check `paragu-ai-builder/src/registry/<type>.type.json` exists — if "⚠" or "🆕", escalate to §4.
4. Create `sites/<tenant-slug>/site.json` with `vertical` and `businessType` set from the lookup.
5. Copy content from `src/content/<vertical>.content.json` as the starting scaffold.

### When planning the next lead scrape
Order the unscraped optgroups in §5 by ACV × reachability. Early candidates: Medicina y Salud (high ACV, regulated), Viajes y Turismo (medium ACV, digital-native), Fiestas y Eventos (seasonal, Messaging-friendly).

### When the builder registry is extended
Every new `type.json` added should back-populate the "Builder type" column here. Delete the "🆕 gap" row from §4 once a slug is live.

---

*Document created: April 2026 · Source directory: Paraguayan SME directory rubro select · Builder registry version: v3.0.0 · Maintainer: update when rubros, verticals, or registry types change.*
