# DB2ADMIN.WRKPRODUCTIONPROGRESSSPINNING

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `MACHINECODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 131767

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `MACHINECODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 4 | `INITIALREADING` | INTEGER | NOT NULL |  |  |  |
| 5 | `FINALREADING` | INTEGER | NOT NULL |  |  |  |
| 6 | `RDIFFERENCE` | DECIMAL(11,4) |  |  |  |  |
| 7 | `CONVERTEDKG` | DECIMAL(11,4) |  |  |  |  |
| 8 | `HANKCOUNT` | DECIMAL(11,4) |  |  |  |  |
| 9 | `SPINDLES` | BIGINT | NOT NULL |  |  |  |
| 10 | `TOTALDOFFS` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.MACHINECODE,
       t.PRODUCTIONORDERCODE,
       t.INITIALREADING,
       t.FINALREADING,
       t.RDIFFERENCE,
       t.CONVERTEDKG,
       t.HANKCOUNT,
       t.SPINDLES,
       t.TOTALDOFFS
FROM   DB2ADMIN.WRKPRODUCTIONPROGRESSSPINNING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
