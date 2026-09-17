# DB2ADMIN.PRODUCTIONCUSTOMIZEDOPTIONS

- **Module**: `PRODUCTION` (high confidence — table name starts with 'PRODUCTION')
- **Roles**: `business_data`
- **Columns**: 45
- **Primary key**: `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 41273

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PLANTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 2 | `WAREHOUSEWIPHANDLING` | SMALLINT | NOT NULL |  |  |  |
| 3 | `BLOCKSHANDLING` | SMALLINT | NOT NULL |  |  |  |
| 4 | `CURRENTYEAR` | DECIMAL(4,0) |  |  |  |  |
| 5 | `FUTUREYEAR` | DECIMAL(4,0) |  |  |  |  |
| 6 | `AUTOMATICRESERVATIONISSUE` | SMALLINT | NOT NULL |  |  |  |
| 7 | `PRODUCTIONDEMANDCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 8 | `ADSTEPGROUPINGNUMBER` | INTEGER | NOT NULL |  |  |  |
| 9 | `COUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 10 | `STFIRSTEVOLUTIONLABEL` | VARCHAR(80) |  |  |  |  |
| 11 | `STSECONDEVOLUTIONLABEL` | VARCHAR(80) |  |  |  |  |
| 12 | `STTHIRDEVOLUTIONLABEL` | VARCHAR(80) |  |  |  |  |
| 13 | `STFOURTHEVOLUTIONLABEL` | VARCHAR(80) |  |  |  |  |
| 14 | `STEPGROUPINGCODE` | CHAR(20) |  |  |  |  |
| 15 | `STEPGROUPINGFORDEMANDCODE` | CHAR(20) |  |  |  |  |
| 16 | `ORDERCOUNTERCODE` | CHAR(20) |  |  |  |  |
| 17 | `DEMANDCUSTOMIZEUICODE` | CHAR(20) |  |  |  |  |
| 18 | `RESERVATIONCUSTOMIZEUICODE` | CHAR(20) |  |  |  |  |
| 19 | `STEPCUSTOMIZEUICODE` | CHAR(20) |  |  |  |  |
| 20 | `CHECKDEMANDCODE` | CHAR(20) |  |  |  |  |
| 21 | `CHECKRESERVATIONCODE` | CHAR(20) |  |  |  |  |
| 22 | `CHECKSTEPCODE` | CHAR(20) |  |  |  |  |
| 23 | `CHECKORDERCODE` | CHAR(20) |  |  |  |  |
| 24 | `ADSTEPVALORIZATIONCODE` | CHAR(20) |  |  |  |  |
| 25 | `SPLITRECEIPTQTYRULECODE` | CHAR(20) |  |  |  |  |
| 26 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 27 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 28 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 29 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 30 | `PLANTCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 31 | `PRODEMANDCOUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 32 | `COUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 33 | `PRODPLANNINGCHECKCODE` | CHAR(20) |  |  |  |  |
| 34 | `PROPROGRESSIMPSENDEMAILFLAG` | SMALLINT | NOT NULL |  |  |  |
| 35 | `PROPROGRESSIMPLETTERTMPCODE` | CHAR(30) |  | FK | foreign_key |  |
| 36 | `PROPROGRESSIMPEMAILRECIPIENT` | CHAR(60) |  |  |  |  |
| 37 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 38 | `MQMMCMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 39 | `PRDIMPEXPORTMANAGERPOLICYCODE` | CHAR(20) |  |  |  |  |
| 40 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 41 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 42 | `RESERVATIONORGANIZERCNTCMYCOD` | CHAR(3) |  | FK | foreign_key |  |
| 43 | `RESERVATIONORGANIZERCNTCODE` | CHAR(8) |  | FK | foreign_key |  |
| 44 | `TNAMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSLETTERTEMPLATE_PRODUCTIONPROGRESSIMPORTLETTERTEMPLATE` | `COMPANYCODE`, `PROPROGRESSIMPLETTERTMPCODE` | [`ABSLETTERTEMPLATE`](../PLATFORM/ABSLETTERTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTIONCUSTOMIZEDOPTIONS.COMPANYCODE = ABSLETTERTEMPLATE.COMPANYCODE AND PRODUCTIONCUSTOMIZEDOPTIONS.PROPROGRESSIMPLETTERTMPCODE = ABSLETTERTEMPLATE.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRODUCTIONCUSTOMIZEDOPTIONS.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_COUNTER` | `COUNTERCOMPANYCODE`, `COUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTIONCUSTOMIZEDOPTIONS.COUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND PRODUCTIONCUSTOMIZEDOPTIONS.COUNTERCODE = COUNTER.CODE` |
| `COUNTER_PRODUCTIONDEMANDCOUNTER` | `PRODEMANDCOUNTERCOMPANYCODE`, `PRODUCTIONDEMANDCOUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTIONCUSTOMIZEDOPTIONS.PRODEMANDCOUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND PRODUCTIONCUSTOMIZEDOPTIONS.PRODUCTIONDEMANDCOUNTERCODE = COUNTER.CODE` |
| `COUNTER_RESERVATIONORGANIZERCOUNTER` | `RESERVATIONORGANIZERCNTCMYCOD`, `RESERVATIONORGANIZERCNTCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTIONCUSTOMIZEDOPTIONS.RESERVATIONORGANIZERCNTCMYCOD = COUNTER.COMPANYCODE AND PRODUCTIONCUSTOMIZEDOPTIONS.RESERVATIONORGANIZERCNTCODE = COUNTER.CODE` |
| `PLANT_PLANT` | `PLANTCOMPANYCODE`, `PLANTCODE` | [`PLANT`](../CORE_MASTER/PLANT.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTIONCUSTOMIZEDOPTIONS.PLANTCOMPANYCODE = PLANT.COMPANYCODE AND PRODUCTIONCUSTOMIZEDOPTIONS.PLANTCODE = PLANT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PROCUSTOMIZEDOPTIONSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PLANTCODE,
       t.WAREHOUSEWIPHANDLING,
       t.BLOCKSHANDLING,
       t.CURRENTYEAR,
       t.FUTUREYEAR,
       t.AUTOMATICRESERVATIONISSUE,
       t.PRODUCTIONDEMANDCOUNTERCODE,
       t.ADSTEPGROUPINGNUMBER,
       t.COUNTERCODE,
       t.STFIRSTEVOLUTIONLABEL,
       t.STSECONDEVOLUTIONLABEL
FROM   DB2ADMIN.PRODUCTIONCUSTOMIZEDOPTIONS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
