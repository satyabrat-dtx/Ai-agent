# DB2ADMIN.WRKSALESSHIPPINGRETURN

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 80690

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `STOCKTRNTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 5 | `STOCKTRNTRNDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 6 | `ORIGORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 7 | `ORIGORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 8 | `ORIGORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 9 | `ORIGORDERSUBLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 10 | `ORIGORDERCOMPONENTLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 11 | `DOCLINELOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 12 | `ORIGORDERCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 13 | `SCLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 14 | `SCLCODE` | CHAR(15) |  |  |  |  |
| 15 | `SCLLINE` | DECIMAL(7,0) |  |  |  |  |
| 16 | `SCLDETAILLINE` | DECIMAL(3,0) |  |  |  |  |
| 17 | `FLAGDETAIL` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.COMPANYCODE,
       t.STOCKTRNTRANSACTIONNUMBER,
       t.STOCKTRNTRNDETAILNUMBER,
       t.ORIGORDERCOUNTERCODE,
       t.ORIGORDERCODE,
       t.ORIGORDERLINE,
       t.ORIGORDERSUBLINE,
       t.ORIGORDERCOMPONENTLINE,
       t.DOCLINELOGICALWAREHOUSECODE
FROM   DB2ADMIN.WRKSALESSHIPPINGRETURN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
