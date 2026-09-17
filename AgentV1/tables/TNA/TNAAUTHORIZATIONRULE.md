# DB2ADMIN.TNAAUTHORIZATIONRULE

- **Module**: `TNA` (low confidence — table name starts with 'TNA')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `TNAAUTHORIZATIONTMPCMYCODE`, `TNAAUTHORIZATIONTEMPLATECODE`, `TNAAUTHORIZATIONTMPUNIQUEID`, `LINENUMBER`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 195441

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TNAAUTHORIZATIONTMPCMYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `TNAAUTHORIZATIONTEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `TNAAUTHORIZATIONTMPUNIQUEID` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINENUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `RULESEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `TNAAUTHORIZATIONTEMPLATE_AUTHORIZATIONRULES` | `TNAAUTHORIZATIONTMPCMYCODE`, `TNAAUTHORIZATIONTEMPLATECODE`, `TNAAUTHORIZATIONTMPUNIQUEID` | [`TNAAUTHORIZATIONTEMPLATE`](../TNA/TNAAUTHORIZATIONTEMPLATE.md) | `COMPANYCODE`, `CODE`, `UNIQUEID` | RESTRICT | `TNAAUTHORIZATIONRULE.TNAAUTHORIZATIONTMPCMYCODE = TNAAUTHORIZATIONTEMPLATE.COMPANYCODE AND TNAAUTHORIZATIONRULE.TNAAUTHORIZATIONTEMPLATECODE = TNAAUTHORIZATIONTEMPLATE.CODE AND TNAAUTHORIZATIONRULE.TNAAUTHORIZATIONTMPUNIQUEID = TNAAUTHORIZATIONTEMPLATE.UNIQUEID` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `TNAAUTHORIZATIONRULE_FIELDS` | [`TNAAUTHORIZATIONRULEFIELD`](../TNA/TNAAUTHORIZATIONRULEFIELD.md) | `COMPANY`, `TEMPLATECODE`, `TNAUNIQUEID`, `LINE` | `TNAAUTHORIZATIONRULEFIELD.COMPANY = TNAAUTHORIZATIONRULE.TNAAUTHORIZATIONTMPCMYCODE AND TNAAUTHORIZATIONRULEFIELD.TEMPLATECODE = TNAAUTHORIZATIONRULE.TNAAUTHORIZATIONTEMPLATECODE AND TNAAUTHORIZATIONRULEFIELD.TNAUNIQUEID = TNAAUTHORIZATIONRULE.TNAAUTHORIZATIONTMPUNIQUEID AND TNAAUTHORIZATIONRULEFIELD.LINE = TNAAUTHORIZATIONRULE.LINENUMBER` |

## Indexes

- `TNAAUTHORIZATIONRULEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TNAAUTHORIZATIONTMPCMYCODE,
       t.TNAAUTHORIZATIONTEMPLATECODE,
       t.TNAAUTHORIZATIONTMPUNIQUEID,
       t.LINENUMBER,
       t.RULESEQUENCE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.TNAAUTHORIZATIONRULE t
FETCH FIRST 100 ROWS ONLY;
```
