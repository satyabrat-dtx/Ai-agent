# DB2ADMIN.COSTELEMENTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `COSTING` (high confidence — table name starts with 'COST')
- **Roles**: `staging_mirror`
- **Columns**: 36
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 62510

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 4 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 5 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 6 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 7 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 8 | `COSTCATEGORYCODE` | CHAR(20) |  |  |  |  |
| 9 | `COSTLEVELCODE` | CHAR(3) |  |  |  |  |
| 10 | `VALUATIONTYPE` | CHAR(2) |  |  |  |  |
| 11 | `DATASET` | CHAR(5) |  |  |  |  |
| 12 | `PRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 13 | `INDUSTRIALACCOUNTINGCODE` | CHAR(20) |  |  |  |  |
| 14 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 15 | `ALLOWEDDIVISIONSSTR` | VARCHAR(100) |  |  |  |  |
| 16 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 17 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 18 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 19 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 20 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 21 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 22 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 23 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 24 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 25 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 26 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 27 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 28 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 29 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 30 | `COSTTYPE` | CHAR(1) |  |  |  |  |
| 31 | `SERVICEITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 32 | `SERVICESUBCODE01` | CHAR(20) |  |  |  |  |
| 33 | `MAINCOSTELEFORSERVICEEXTOP` | SMALLINT | NOT NULL |  |  |  |
| 34 | `SELLINGCOST` | SMALLINT | NOT NULL |  |  |  |
| 35 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COSTELEMENTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.COSTCATEGORYCODE,
       t.COSTLEVELCODE,
       t.VALUATIONTYPE,
       t.DATASET
FROM   DB2ADMIN.COSTELEMENTBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
