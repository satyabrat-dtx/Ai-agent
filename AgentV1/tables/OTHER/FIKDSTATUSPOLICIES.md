# DB2ADMIN.FIKDSTATUSPOLICIES

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `UNIQUEID`, `COMPANYCODE`, `ITEMTYPECODE`, `STATUSCODE`, `STATUSRULELINENR`, `SUBLINE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 190275

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
| 7 | `ENABLED` | SMALLINT | NOT NULL |  |  |  |
| 8 | `ISRULEPRIMARYKEY` | SMALLINT | NOT NULL |  |  |  |
| 9 | `FORCEDSTATUS` | SMALLINT | NOT NULL |  |  |  |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 12 | `AUTOMATIC` | SMALLINT | NOT NULL |  |  |  |
| 13 | `NOSTATUSMANAGED` | INTEGER | NOT NULL |  |  |  |
| 14 | `ISCONFIGROW` | SMALLINT | NOT NULL |  |  |  |
| 15 | `BATCHLOCK` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FIKDSTATUSPOLICIES.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FIKDSTATUSPOLICIES.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND FIKDSTATUSPOLICIES.ITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FIKDSTATUSPOLICIESUID` (ABSUNIQUEID)
- `FIKDSTATUSPOLI1` (UNIQUEID, ENABLED, COMPANYCODE, ISCONFIGROW, SEQUENCE, ITEMTYPECODE, STATUSCODE, STATUSRULELINENR, SUBLINE)

## Starter query

```sql
SELECT t.UNIQUEID,
       t.COMPANYCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.STATUSCODE,
       t.STATUSRULELINENR,
       t.SUBLINE,
       t.ENABLED,
       t.ISRULEPRIMARYKEY,
       t.FORCEDSTATUS,
       t.ABSUNIQUEID,
       t.SEQUENCE
FROM   DB2ADMIN.FIKDSTATUSPOLICIES t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
