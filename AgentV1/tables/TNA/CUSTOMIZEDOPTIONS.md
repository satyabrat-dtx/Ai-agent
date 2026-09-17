# DB2ADMIN.CUSTOMIZEDOPTIONS

- **Module**: `TNA` (low confidence — FK neighbourhood: 1 of 1 related tables are TNA)
- **Roles**: `business_data`
- **Columns**: 63
- **Primary key**: `CODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 42762

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(30) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `FIRSTCONTACBOOKLINEDESCRIPTION` | CHAR(30) |  |  |  |  |
| 2 | `SNDCONTACBOOKLINEDESCRIPTION` | CHAR(30) |  |  |  |  |
| 3 | `THIRDCONTACBOOKLINEDESCRIPTION` | CHAR(30) |  |  |  |  |
| 4 | `FOURTHCONTACBOOKLINEDES` | CHAR(30) |  |  |  |  |
| 5 | `FIFTHCONTACBOOKLINEDESCRIPTION` | CHAR(30) |  |  |  |  |
| 6 | `FIRSTADDRESSLINEDESCRIPTION` | CHAR(30) | NOT NULL |  |  |  |
| 7 | `SECONDADDRESSLINEDESCRIPTION` | CHAR(30) |  |  |  |  |
| 8 | `THIRDADDRESSLINEDESCRIPTION` | CHAR(30) |  |  |  |  |
| 9 | `FOURTHADDRESSLINEDESCRIPTION` | CHAR(30) |  |  |  |  |
| 10 | `FIFTHADDRESSLINEDESCRIPTION` | CHAR(30) |  |  |  |  |
| 11 | `POSTALCODEDESCRIPTION` | CHAR(30) |  |  |  |  |
| 12 | `TOWNDESCRIPTION` | CHAR(30) |  |  |  |  |
| 13 | `DISTRICTDESCRIPTION` | CHAR(30) |  |  |  |  |
| 14 | `BANKCODEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 15 | `BANKEXTERNALCODEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 16 | `ORDERBANKPOLICYCODE` | CHAR(20) |  |  |  |  |
| 17 | `EXPORTCODE` | CHAR(20) |  |  |  |  |
| 18 | `CHARACTERFORNUMBER` | SMALLINT | NOT NULL |  |  |  |
| 19 | `CHARACTERFORONE` | CHAR(1) |  |  |  |  |
| 20 | `CHARACTERFORTWO` | CHAR(1) |  |  |  |  |
| 21 | `CHARACTERFORTHREE` | CHAR(1) |  |  |  |  |
| 22 | `CHARACTERFORFOUR` | CHAR(1) |  |  |  |  |
| 23 | `CHARACTERFORFIVE` | CHAR(1) |  |  |  |  |
| 24 | `CHARACTERFORSIX` | CHAR(1) |  |  |  |  |
| 25 | `CHARACTERFORSEVEN` | CHAR(1) |  |  |  |  |
| 26 | `CHARACTERFOREIGHT` | CHAR(1) |  |  |  |  |
| 27 | `CHARACTERFORNINE` | CHAR(1) |  |  |  |  |
| 28 | `CHARACTERFORZERO` | CHAR(1) |  |  |  |  |
| 29 | `SALESEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |
| 30 | `PURCHASEEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |
| 31 | `EXCHANGERATEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 32 | `BUSINESSPARTNERLOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 33 | `ADDRESSLOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 34 | `ELEMENTSLOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 35 | `BUSINESSPARTNERCUSTOMIZEUICODE` | CHAR(20) |  |  |  |  |
| 36 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 37 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 38 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 39 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 40 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 41 | `PRINTANDMAILCODE` | CHAR(20) |  |  |  |  |
| 42 | `LITERUNITOFMEASURECODE` | CHAR(3) |  | FK | foreign_key |  |
| 43 | `KILOGRAMUNITOFMEASURECODE` | CHAR(3) |  | FK | foreign_key |  |
| 44 | `VALUATIONEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |
| 45 | `SALESTAXLISTEXCHANGERATE` | SMALLINT | NOT NULL |  |  |  |
| 46 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 47 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 48 | `STARTHOURWORKINGDAYFROMSHIFT` | SMALLINT | NOT NULL |  |  |  |
| 49 | `TNAMANAGEDBYCOMPANY` | SMALLINT | NOT NULL |  |  |  |
| 50 | `TASKINLATE` | SMALLINT | NOT NULL |  |  |  |
| 51 | `NROFDAYSFORPENDINGSTATUS` | INTEGER | NOT NULL |  |  |  |
| 52 | `MESSAGETYPE` | INTEGER | NOT NULL |  |  |  |
| 53 | `ACTIVITYRESULTTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 54 | `ACTIVITYRESULTTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 55 | `REQUIRECOLORAPPROVAL` | SMALLINT | NOT NULL |  |  |  |
| 56 | `EXCINVITEMSLOOKUP` | SMALLINT | NOT NULL |  |  |  |
| 57 | `COPYALSONOTOPTIONALTASK` | SMALLINT | NOT NULL |  |  |  |
| 58 | `PREFIXCAROUSELFOROBJECT` | CHAR(10) |  |  |  |  |
| 59 | `PREFIXCAROUSELFORCOLLECTION` | CHAR(10) |  |  |  |  |
| 60 | `PREFIXCAROUSELALL` | CHAR(10) |  |  |  |  |
| 61 | `GRIDIMAGEWIDTH` | CHAR(10) |  |  |  |  |
| 62 | `GRIDIMAGEHEIGTH` | CHAR(10) |  |  |  |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ACTIVITYRESULTTYPE_ACTIVITYRESULTTYPE` | `ACTIVITYRESULTTYPECOMPANYCODE`, `ACTIVITYRESULTTYPECODE` | [`ACTIVITYRESULTTYPE`](../TNA/ACTIVITYRESULTTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `CUSTOMIZEDOPTIONS.ACTIVITYRESULTTYPECOMPANYCODE = ACTIVITYRESULTTYPE.COMPANYCODE AND CUSTOMIZEDOPTIONS.ACTIVITYRESULTTYPECODE = ACTIVITYRESULTTYPE.CODE` |
| `UNITOFMEASURE_KILOGRAMUNITOFMEASURE` | `KILOGRAMUNITOFMEASURECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `CUSTOMIZEDOPTIONS.KILOGRAMUNITOFMEASURECODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_LITERUNITOFMEASURE` | `LITERUNITOFMEASURECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `CUSTOMIZEDOPTIONS.LITERUNITOFMEASURECODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CUSTOMIZEDOPTIONSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.FIRSTCONTACBOOKLINEDESCRIPTION,
       t.SNDCONTACBOOKLINEDESCRIPTION,
       t.THIRDCONTACBOOKLINEDESCRIPTION,
       t.FOURTHCONTACBOOKLINEDES,
       t.FIFTHCONTACBOOKLINEDESCRIPTION,
       t.FIRSTADDRESSLINEDESCRIPTION,
       t.SECONDADDRESSLINEDESCRIPTION,
       t.THIRDADDRESSLINEDESCRIPTION,
       t.FOURTHADDRESSLINEDESCRIPTION,
       t.FIFTHADDRESSLINEDESCRIPTION,
       t.POSTALCODEDESCRIPTION
FROM   DB2ADMIN.CUSTOMIZEDOPTIONS t
FETCH FIRST 100 ROWS ONLY;
```
