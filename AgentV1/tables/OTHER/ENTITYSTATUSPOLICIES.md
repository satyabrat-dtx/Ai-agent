# DB2ADMIN.ENTITYSTATUSPOLICIES

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `UNIQUEID`, `COMPANYCODE`, `ITEMTYPECODE`, `STATUSCODE`, `STATUSRULELINENR`, `SUBLINE`, `SUFFIXCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 194513

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `STATUSCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `STATUSRULELINENR` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `SUBLINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 7 | `SUFFIXCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 8 | `ENABLED` | SMALLINT | NOT NULL |  |  |  |
| 9 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 10 | `AUTOMATIC` | SMALLINT | NOT NULL |  |  |  |
| 11 | `ISCONFIGROW` | SMALLINT | NOT NULL |  |  |  |
| 12 | `BATCHLOCK` | SMALLINT | NOT NULL |  |  |  |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ENTITYSTATUSPOLICIES.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ENTITYSTATUSPOLICIES.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND ENTITYSTATUSPOLICIES.ITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ENTITYSTATUSPOLICIESUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.UNIQUEID,
       t.COMPANYCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.STATUSCODE,
       t.STATUSRULELINENR,
       t.SUBLINE,
       t.SUFFIXCODE,
       t.ENABLED,
       t.SEQUENCE,
       t.AUTOMATIC,
       t.ISCONFIGROW
FROM   DB2ADMIN.ENTITYSTATUSPOLICIES t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
