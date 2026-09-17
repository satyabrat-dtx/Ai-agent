# DB2ADMIN.PDMDB1HBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PDM` (medium confidence — table name starts with 'PDM')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 31
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 75343

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `DBRECTYCODE` | CHAR(3) |  |  |  |  |
| 4 | `DBTPREC` | DECIMAL(1,0) |  |  |  |  |
| 5 | `DBCITEM` | CHAR(15) |  |  |  |  |
| 6 | `DBVERNR` | CHAR(3) |  |  |  |  |
| 7 | `DBVERST` | DECIMAL(3,0) |  |  |  |  |
| 8 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 10 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 20 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 21 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 22 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 23 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 24 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 25 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 26 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 27 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 28 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 29 | `DBSUBFX` | CHAR(20) |  |  |  |  |
| 30 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `PDMDB1HBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `PDMDB1HBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.DBRECTYCODE,
       t.DBTPREC,
       t.DBCITEM,
       t.DBVERNR,
       t.DBVERST,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03
FROM   DB2ADMIN.PDMDB1HBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
