# DB2ADMIN.WRKREPORTGROUPING

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `CREATIONTIMESTAMP`, `CREATIONUSER`, `LINE`, `INVOICETYPECODE`, `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 145990

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `INVOICETYPECODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `COMPANYCODE` | CHAR(20) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 5 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 6 | `SUBCODE1` | CHAR(20) |  |  |  |  |
| 7 | `SUBCODE2` | CHAR(10) |  |  |  |  |
| 8 | `SUBCODE3` | CHAR(10) |  |  |  |  |
| 9 | `SUBCODE4` | CHAR(10) |  |  |  |  |
| 10 | `SUBCODE5` | CHAR(10) |  |  |  |  |
| 11 | `SUBCODE6` | CHAR(10) |  |  |  |  |
| 12 | `SUBCODE7` | CHAR(10) |  |  |  |  |
| 13 | `SUBCODE8` | CHAR(10) |  |  |  |  |
| 14 | `SUBCODE9` | CHAR(10) |  |  |  |  |
| 15 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `PRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 17 | `PRIMARYUMCODE` | CHAR(3) |  |  |  |  |
| 18 | `SECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 19 | `SECODARYUMCODE` | CHAR(3) |  |  |  |  |
| 20 | `PACKINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 21 | `PACKINGUMCODE` | CHAR(3) |  |  |  |  |
| 22 | `PRICE` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.INVOICETYPECODE,
       t.COMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE1,
       t.SUBCODE2,
       t.SUBCODE3,
       t.SUBCODE4,
       t.SUBCODE5,
       t.SUBCODE6
FROM   DB2ADMIN.WRKREPORTGROUPING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
