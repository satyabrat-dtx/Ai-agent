# DB2ADMIN.AUTHORIZATIONRULE

- **Module**: `TNA` (low confidence — FK neighbourhood: 1 of 1 related tables are TNA)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `AUTHORIZATIONTMPCOMPANYCODE`, `AUTHORIZATIONTEMPLATECODE`, `LINENUMBER`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 191275

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `AUTHORIZATIONTMPCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `AUTHORIZATIONTEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINENUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `RULESEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 8 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 9 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `AUTHORIZATIONTEMPLATE_AUTHORIZATIONRULES` | `AUTHORIZATIONTMPCOMPANYCODE`, `AUTHORIZATIONTEMPLATECODE` | [`AUTHORIZATIONTEMPLATE`](../TNA/AUTHORIZATIONTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `AUTHORIZATIONRULE.AUTHORIZATIONTMPCOMPANYCODE = AUTHORIZATIONTEMPLATE.COMPANYCODE AND AUTHORIZATIONRULE.AUTHORIZATIONTEMPLATECODE = AUTHORIZATIONTEMPLATE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `AUTHORIZATIONRULE_FIELDS` | [`AUTHORIZATIONRULEFIELD`](../TNA/AUTHORIZATIONRULEFIELD.md) | `COMPANYCODE`, `TEMPLATECODE`, `LINE` | `AUTHORIZATIONRULEFIELD.COMPANYCODE = AUTHORIZATIONRULE.AUTHORIZATIONTMPCOMPANYCODE AND AUTHORIZATIONRULEFIELD.TEMPLATECODE = AUTHORIZATIONRULE.AUTHORIZATIONTEMPLATECODE AND AUTHORIZATIONRULEFIELD.LINE = AUTHORIZATIONRULE.LINENUMBER` |

## Indexes

- `AUTHORIZATIONRULEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.AUTHORIZATIONTMPCOMPANYCODE,
       t.AUTHORIZATIONTEMPLATECODE,
       t.LINENUMBER,
       t.RULESEQUENCE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.AUTHORIZATIONRULE t
FETCH FIRST 100 ROWS ONLY;
```
