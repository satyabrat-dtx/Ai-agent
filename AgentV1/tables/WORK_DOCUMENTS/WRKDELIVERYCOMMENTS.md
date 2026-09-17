# DB2ADMIN.WRKDELIVERYCOMMENTS

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `COUNTERCODE`, `ORDERCODE`, `ORDERLINE`, `ORDERSUBLINE`, `COMPONENTORDERLINE`, `DELIVERYLINE`, `ORIGIN`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 3728

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `ORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 5 | `ORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 6 | `COMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 7 | `DELIVERYLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 8 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 9 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 10 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 11 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.COUNTERCODE,
       t.ORDERCODE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.COMPONENTORDERLINE,
       t.DELIVERYLINE,
       t.ORIGIN,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE
FROM   DB2ADMIN.WRKDELIVERYCOMMENTS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
