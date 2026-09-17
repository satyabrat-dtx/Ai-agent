# DB2ADMIN.WRKRG23ICOBH

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `EXCISEYEARREGNO`, `EXCISEYEARCODE`, `ITEMTYPECODE`, `SUBCODE1`, `SUBCODE2`, `SUBCODE3`, `SUBCODE4`, `SUBCODE5`, `SUBCODE6`, `SUBCODE7`, `SUBCODE8`, `SUBCODE9`, `SUBCODE10`, `TARIFFCODE`, `PLANTCODE`, `QUANTITYUMCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 145934

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `EXCISEYEARREGNO` | CHAR(30) | NOT NULL | PK | primary_key |  |
| 3 | `EXCISEYEARCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `SUBCODE1` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 6 | `SUBCODE2` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 7 | `SUBCODE3` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 8 | `SUBCODE4` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 9 | `SUBCODE5` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 10 | `SUBCODE6` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 11 | `SUBCODE7` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 12 | `SUBCODE8` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 13 | `SUBCODE9` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 14 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 15 | `TARIFFCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 16 | `PLANTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 17 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 18 | `QUANTITYUMCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 19 | `CODE` | INTEGER | NOT NULL |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.EXCISEYEARREGNO,
       t.EXCISEYEARCODE,
       t.ITEMTYPECODE,
       t.SUBCODE1,
       t.SUBCODE2,
       t.SUBCODE3,
       t.SUBCODE4,
       t.SUBCODE5,
       t.SUBCODE6,
       t.SUBCODE7
FROM   DB2ADMIN.WRKRG23ICOBH t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
