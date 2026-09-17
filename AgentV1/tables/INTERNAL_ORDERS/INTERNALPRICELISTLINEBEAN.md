# DB2ADMIN.INTERNALPRICELISTLINEBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `INTERNAL_ORDERS` (high confidence — table name starts with 'INTERNAL')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 79
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 86876

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 2 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 3 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 4 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 5 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 6 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 7 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `VALIDFROMDATE` | DATE |  |  |  |  |
| 12 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 13 | `PRICEUOMCODE` | CHAR(3) |  |  |  |  |
| 14 | `VALIDTODATE` | DATE |  |  |  |  |
| 15 | `QUANTITYLIMITFROM` | DECIMAL(15,5) |  |  |  |  |
| 16 | `QUANTITYLIMITTO` | DECIMAL(15,5) |  |  |  |  |
| 17 | `SELECTPRIMORSEC` | INTEGER | NOT NULL |  |  |  |
| 18 | `PRICECHANGEOVER` | DECIMAL(5,2) |  |  |  |  |
| 19 | `EVERYQTYADD` | DECIMAL(9,0) |  |  |  |  |
| 20 | `PRICECHANGEUNDER` | DECIMAL(5,2) |  |  |  |  |
| 21 | `EVERYQTYSUB` | DECIMAL(9,0) |  |  |  |  |
| 22 | `LOWESTPRICE` | DECIMAL(18,5) |  |  |  |  |
| 23 | `PRICE1` | DECIMAL(18,5) |  |  |  |  |
| 24 | `QUANTITYLIMIT1FROM` | DECIMAL(15,5) |  |  |  |  |
| 25 | `QUANTITYLIMIT1TO` | DECIMAL(15,5) |  |  |  |  |
| 26 | `PRICE2` | DECIMAL(18,5) |  |  |  |  |
| 27 | `QUANTITYLIMIT2FROM` | DECIMAL(9,0) |  |  |  |  |
| 28 | `QUANTITYLIMIT2TO` | DECIMAL(15,5) |  |  |  |  |
| 29 | `PRICE3` | DECIMAL(18,5) |  |  |  |  |
| 30 | `QUANTITYLIMIT3FROM` | DECIMAL(9,0) |  |  |  |  |
| 31 | `QUANTITYLIMIT3TO` | DECIMAL(15,5) |  |  |  |  |
| 32 | `PRICE4` | DECIMAL(18,5) |  |  |  |  |
| 33 | `QUANTITYLIMIT4FROM` | DECIMAL(9,0) |  |  |  |  |
| 34 | `QUANTITYLIMIT4TO` | DECIMAL(15,5) |  |  |  |  |
| 35 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 36 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 37 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 38 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 39 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 40 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 41 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 42 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 43 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 44 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 45 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 46 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 47 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 48 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 49 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 50 | `USECREATIONUSER` | SMALLINT | NOT NULL |  |  |  |
| 51 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 52 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 53 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 54 | `PERCENTCATEGORY1` | DECIMAL(6,3) |  |  |  |  |
| 55 | `PERCENTCATEGORY2` | DECIMAL(6,3) |  |  |  |  |
| 56 | `PERCENTCATEGORY3` | DECIMAL(6,3) |  |  |  |  |
| 57 | `PERCENTCATEGORY4` | DECIMAL(6,3) |  |  |  |  |
| 58 | `PERCENTCATEGORY5` | DECIMAL(6,3) |  |  |  |  |
| 59 | `PERCENTCATEGORY6` | DECIMAL(6,3) |  |  |  |  |
| 60 | `PERCENTCATEGORY7` | DECIMAL(6,3) |  |  |  |  |
| 61 | `PERCENTCATEGORY8` | DECIMAL(6,3) |  |  |  |  |
| 62 | `PERCENTCATEGORY9` | DECIMAL(6,3) |  |  |  |  |
| 63 | `PERCENTCATEGORY10` | DECIMAL(6,3) |  |  |  |  |
| 64 | `PERCENTCATEGORY11` | DECIMAL(6,3) |  |  |  |  |
| 65 | `PERCENTCATEGORY12` | DECIMAL(6,3) |  |  |  |  |
| 66 | `PERCENTCATEGORY0` | DECIMAL(6,3) |  |  |  |  |
| 67 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 68 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 69 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 70 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 71 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 72 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 73 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |
| 74 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 75 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 76 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 77 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 78 | `ALLOWZEROPRICE` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **INTERNALPRICELIST**.`ABSUNIQUEID` (high confidence — name = 'INTERNALPRICELIST' + known child suffix 'LINE')
  - JOIN predicate: `INTERNALPRICELISTLINEBEAN.FATHERID = INTERNALPRICELIST.ABSUNIQUEID`

## Indexes

- `INTERNALPRICELISTLINEBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08,
       t.SUBCODE09,
       t.SUBCODE10,
       t.VALIDFROMDATE
FROM   DB2ADMIN.INTERNALPRICELISTLINEBEAN t
FETCH FIRST 100 ROWS ONLY;
```
