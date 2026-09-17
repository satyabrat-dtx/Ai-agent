# DB2ADMIN.PRODUCTIONDEMANDELEMENTSBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PRODUCTION` (high confidence — table name starts with 'PRODUCTION')
- **Roles**: `staging_mirror`
- **Columns**: 32
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 120719

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 3 | `DEMANDCODE` | CHAR(15) |  |  |  |  |
| 4 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 5 | `ELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 6 | `ELEMENTCODE` | CHAR(15) |  |  |  |  |
| 7 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 8 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 9 | `USERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 10 | `USERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 11 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 12 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 13 | `USERSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 14 | `USERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 15 | `USERPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 16 | `USERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 17 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 18 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 19 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 20 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 21 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 22 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 23 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 24 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 25 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 26 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 27 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 28 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 29 | `CUTTINGLINECUTTINGHDRCNTCODE` | CHAR(8) |  |  |  |  |
| 30 | `CUTTINGLINECUTTINGHEADERCODE` | CHAR(15) |  |  |  |  |
| 31 | `CUTTINGLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRODEMANDELEMENTSBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.DEMANDCOUNTERCODE,
       t.DEMANDCODE,
       t.ITEMTYPEAFICODE,
       t.ELEMENTSUBCODEKEY,
       t.ELEMENTCODE,
       t.BASEPRIMARYQUANTITY,
       t.BASEPRIMARYUOMCODE,
       t.USERPRIMARYQUANTITY,
       t.USERPRIMARYUOMCODE,
       t.BASESECONDARYQUANTITY
FROM   DB2ADMIN.PRODUCTIONDEMANDELEMENTSBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
