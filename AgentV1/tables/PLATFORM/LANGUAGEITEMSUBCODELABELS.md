# DB2ADMIN.LANGUAGEITEMSUBCODELABELS

- **Module**: `PLATFORM` (medium confidence — table name starts with 'LANGUAGE')
- **Roles**: `child_of_implicit_parent`, `translation`
- **Columns**: 12
- **Primary key**: `FATHERID`, `LANGUAGECODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 24789

> Per-language text for a parent row addressed via FATHERID.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL | PK | primary_key implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `LANGUAGECODE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 2 | `SUBCODE01LABEL` | VARCHAR(80) |  |  |  |  |
| 3 | `SUBCODE02LABEL` | VARCHAR(80) |  |  |  |  |
| 4 | `SUBCODE03LABEL` | VARCHAR(80) |  |  |  |  |
| 5 | `SUBCODE04LABEL` | VARCHAR(80) |  |  |  |  |
| 6 | `SUBCODE05LABEL` | VARCHAR(80) |  |  |  |  |
| 7 | `SUBCODE06LABEL` | VARCHAR(80) |  |  |  |  |
| 8 | `SUBCODE07LABEL` | VARCHAR(80) |  |  |  |  |
| 9 | `SUBCODE08LABEL` | VARCHAR(80) |  |  |  |  |
| 10 | `SUBCODE09LABEL` | VARCHAR(80) |  |  |  |  |
| 11 | `SUBCODE10LABEL` | VARCHAR(80) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LANGUAGEITEMSUBCODELABELS.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.FATHERID,
       t.LANGUAGECODE,
       t.SUBCODE01LABEL,
       t.SUBCODE02LABEL,
       t.SUBCODE03LABEL,
       t.SUBCODE04LABEL,
       t.SUBCODE05LABEL,
       t.SUBCODE06LABEL,
       t.SUBCODE07LABEL,
       t.SUBCODE08LABEL,
       t.SUBCODE09LABEL,
       t.SUBCODE10LABEL
FROM   DB2ADMIN.LANGUAGEITEMSUBCODELABELS t
FETCH FIRST 100 ROWS ONLY;
```
