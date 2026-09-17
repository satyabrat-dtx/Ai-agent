# DB2ADMIN.RG23IBALANCE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `TARIFFCODE`, `TYPE`, `ITEMTYPECODE`, `SUBCODE1`, `SUBCODE2`, `SUBCODE3`, `SUBCODE4`, `SUBCODE5`, `SUBCODE6`, `SUBCODE7`, `SUBCODE8`, `SUBCODE9`, `SUBCODE10`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 142749

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `TARIFFCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 3 | `TYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 4 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 5 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `SUBCODE1` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 7 | `SUBCODE2` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 8 | `SUBCODE3` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 9 | `SUBCODE4` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 10 | `SUBCODE5` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 11 | `SUBCODE6` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 12 | `SUBCODE7` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 13 | `SUBCODE8` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 14 | `SUBCODE9` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 15 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 16 | `BALANCE` | DECIMAL(15,5) |  |  |  |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RG23IBALANCE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RG23IBALANCEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.TARIFFCODE,
       t.TYPE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE1,
       t.SUBCODE2,
       t.SUBCODE3,
       t.SUBCODE4,
       t.SUBCODE5,
       t.SUBCODE6
FROM   DB2ADMIN.RG23IBALANCE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
