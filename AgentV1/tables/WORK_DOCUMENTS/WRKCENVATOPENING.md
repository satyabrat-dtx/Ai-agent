# DB2ADMIN.WRKCENVATOPENING

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `RG23IICODE`, `EXCISEYEARREGNO`, `EXCISEYEARCODE`, `LINENO`, `CREATIONTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 144289

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `RG23IICODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `EXCISEYEARREGNO` | CHAR(30) | NOT NULL | PK | primary_key |  |
| 4 | `EXCISEYEARCODE` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 5 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 7 | `HEADING0` | CHAR(15) |  |  |  |  |
| 8 | `OBAMOUNT0` | DECIMAL(18,5) |  |  |  |  |
| 9 | `HEADING1` | CHAR(15) |  |  |  |  |
| 10 | `OBAMOUNT1` | DECIMAL(18,5) |  |  |  |  |
| 11 | `HEADING2` | CHAR(15) |  |  |  |  |
| 12 | `OBAMOUNT2` | DECIMAL(18,5) |  |  |  |  |
| 13 | `HEADING3` | CHAR(15) |  |  |  |  |
| 14 | `OBAMOUNT3` | DECIMAL(18,5) |  |  |  |  |
| 15 | `HEADING4` | CHAR(15) |  |  |  |  |
| 16 | `OBAMOUNT4` | DECIMAL(18,5) |  |  |  |  |
| 17 | `HEADING5` | CHAR(15) |  |  |  |  |
| 18 | `OBAMOUNT5` | DECIMAL(18,5) |  |  |  |  |
| 19 | `HEADING6` | CHAR(15) |  |  |  |  |
| 20 | `OBAMOUNT6` | DECIMAL(18,5) |  |  |  |  |
| 21 | `HEADING7` | CHAR(15) |  |  |  |  |
| 22 | `OBAMOUNT7` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.RG23IICODE,
       t.EXCISEYEARREGNO,
       t.EXCISEYEARCODE,
       t.LINENO,
       t.CREATIONTIMESTAMP,
       t.HEADING0,
       t.OBAMOUNT0,
       t.HEADING1,
       t.OBAMOUNT1,
       t.HEADING2
FROM   DB2ADMIN.WRKCENVATOPENING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
