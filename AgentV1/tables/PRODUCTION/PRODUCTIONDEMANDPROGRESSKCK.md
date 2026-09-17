# DB2ADMIN.PRODUCTIONDEMANDPROGRESSKCK

- **Module**: `PRODUCTION` (high confidence — table name starts with 'PRODUCTION')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANYCODE`, `PRODUCTIONDEMANDCOUNTERCODE`, `BARCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 7954

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PRODUCTIONDEMANDCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `WORKCENTERCODE` | CHAR(8) | NOT NULL |  |  |  |
| 3 | `BARCODE` | CHAR(13) | NOT NULL | PK | primary_key |  |
| 4 | `MACHINECODE` | CHAR(10) |  |  |  |  |
| 5 | `PROCESSEDQUANTITY` | DECIMAL(17,2) |  |  |  |  |
| 6 | `REPROCESSING` | SMALLINT | NOT NULL |  |  |  |
| 7 | `COMMENT` | VARCHAR(60) |  |  |  |  |
| 8 | `PRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 9 | `STEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 10 | `STARTOREND` | CHAR(1) |  |  |  |  |
| 11 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 12 | `PROGRESSDATE` | DATE | NOT NULL |  |  |  |
| 13 | `PROGRESSTIME` | TIME | NOT NULL |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PRODUCTIONDEMANDCOUNTERCODE,
       t.WORKCENTERCODE,
       t.BARCODE,
       t.MACHINECODE,
       t.PROCESSEDQUANTITY,
       t.REPROCESSING,
       t.COMMENT,
       t.PRODUCTIONDEMANDCODE,
       t.STEPNUMBER,
       t.STARTOREND,
       t.OPERATIONCODE
FROM   DB2ADMIN.PRODUCTIONDEMANDPROGRESSKCK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
