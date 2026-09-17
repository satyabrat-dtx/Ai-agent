# DB2ADMIN.LCDETAILBANKDOCUMENT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `COMPANYCODE`, `LCNO`, `LCDATE`, `TUSERGENERICGROUPTYPECODE`, `TCODE`, `DUSERGENERICGROUPTYPECODE`, `DCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 139865

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `LCNO` | CHAR(35) | NOT NULL | PK | primary_key |  |
| 2 | `LCDATE` | DATE | NOT NULL | PK | primary_key |  |
| 3 | `TUSGENGROUPTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 4 | `TUSERGENERICGROUPTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `TCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `DUSGENGROUPTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 7 | `DUSERGENERICGROUPTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 8 | `DCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 9 | `ORIGINAL` | CHAR(15) |  |  |  |  |
| 10 | `COPY` | CHAR(15) |  |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LCDETAILBANKDOCUMENT.COMPANYCODE = COMPANY.CODE` |
| `USERGENERICGROUP_D` | `DUSGENGROUPTYPECOMPANYCODE`, `DUSERGENERICGROUPTYPECODE`, `DCODE` | [`USERGENERICGROUP`](../CORE_MASTER/USERGENERICGROUP.md) | `USERGENGROUPTYPECOMPANYCODE`, `USERGENERICGROUPTYPECODE`, `CODE` | RESTRICT | `LCDETAILBANKDOCUMENT.DUSGENGROUPTYPECOMPANYCODE = USERGENERICGROUP.USERGENGROUPTYPECOMPANYCODE AND LCDETAILBANKDOCUMENT.DUSERGENERICGROUPTYPECODE = USERGENERICGROUP.USERGENERICGROUPTYPECODE AND LCDETAILBANKDOCUMENT.DCODE = USERGENERICGROUP.CODE` |
| `USERGENERICGROUP_T` | `TUSGENGROUPTYPECOMPANYCODE`, `TUSERGENERICGROUPTYPECODE`, `TCODE` | [`USERGENERICGROUP`](../CORE_MASTER/USERGENERICGROUP.md) | `USERGENGROUPTYPECOMPANYCODE`, `USERGENERICGROUPTYPECODE`, `CODE` | RESTRICT | `LCDETAILBANKDOCUMENT.TUSGENGROUPTYPECOMPANYCODE = USERGENERICGROUP.USERGENGROUPTYPECOMPANYCODE AND LCDETAILBANKDOCUMENT.TUSERGENERICGROUPTYPECODE = USERGENERICGROUP.USERGENERICGROUPTYPECODE AND LCDETAILBANKDOCUMENT.TCODE = USERGENERICGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LCDETAILBANKDOCUMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.LCNO,
       t.LCDATE,
       t.TUSGENGROUPTYPECOMPANYCODE,
       t.TUSERGENERICGROUPTYPECODE,
       t.TCODE,
       t.DUSGENGROUPTYPECOMPANYCODE,
       t.DUSERGENERICGROUPTYPECODE,
       t.DCODE,
       t.ORIGINAL,
       t.COPY,
       t.ABSUNIQUEID
FROM   DB2ADMIN.LCDETAILBANKDOCUMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
