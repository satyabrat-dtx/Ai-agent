# DB2ADMIN.FULLITEMWAREHOUSELINKBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 52
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 46691

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 3 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 4 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 5 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 6 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 7 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 15 | `LOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 16 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 17 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 18 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 19 | `ABCCODE` | CHAR(2) |  |  |  |  |
| 20 | `STOCKTAKEPRIORITY` | INTEGER | NOT NULL |  |  |  |
| 21 | `STOCKTAKESTANDARDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 22 | `STOCKTAKECODE` | CHAR(3) |  |  |  |  |
| 23 | `TRNNUMBERFROMLASTSTOCKTAKE` | INTEGER | NOT NULL |  |  |  |
| 24 | `INVENTORYTURNOVERFACTOR` | DECIMAL(11,2) |  |  |  |  |
| 25 | `BASEPRIMARYUNITCODE` | CHAR(3) |  |  |  |  |
| 26 | `REORDERPOINT` | DECIMAL(15,5) |  |  |  |  |
| 27 | `SAFETYSTOCK` | DECIMAL(15,5) |  |  |  |  |
| 28 | `LASTTRANSACTIONDATE` | DATE |  |  |  |  |
| 29 | `LASTENTRYDATE` | DATE |  |  |  |  |
| 30 | `CURRENTSTOCKTAKEDATE` | DATE |  |  |  |  |
| 31 | `LASTSTOCKTAKEDATE` | DATE |  |  |  |  |
| 32 | `UNDERSTOCKTAKE` | CHAR(2) |  |  |  |  |
| 33 | `DIRTYFIELD` | CHAR(20) |  |  |  |  |
| 34 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 35 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 36 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 37 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 38 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 39 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 40 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 41 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 42 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 43 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 44 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 45 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 46 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 47 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 48 | `ENTITYNAME` | CHAR(50) |  |  |  |  |
| 49 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 50 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 51 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FULLITEMWAREHOUSELINKBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08
FROM   DB2ADMIN.FULLITEMWAREHOUSELINKBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
