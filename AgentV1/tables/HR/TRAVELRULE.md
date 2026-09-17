# DB2ADMIN.TRAVELRULE

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `COMPANYCODE`, `ITEMTYPE`, `EMPLOYEEGRADEICSTABLECODE`, `EMPLOYEEGRADECODE`, `EFFECTIVEFROMDATE`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 161897

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `EMPLOYEEGRADEICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `EMPLOYEEGRADECODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `EFFECTIVEFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 5 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TRAVELRULE.COMPANYCODE = COMPANY.CODE` |
| `ICSENTITY_EMPLOYEEGRADE` | `COMPANYCODE`, `EMPLOYEEGRADEICSTABLECODE`, `EMPLOYEEGRADECODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `TRAVELRULE.COMPANYCODE = ICSENTITY.COMPANYCODE AND TRAVELRULE.EMPLOYEEGRADEICSTABLECODE = ICSENTITY.ICSTABLECODE AND TRAVELRULE.EMPLOYEEGRADECODE = ICSENTITY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `TRAVELRULE_LINE` | [`TRAVELRULEDETAIL`](../HR/TRAVELRULEDETAIL.md) | `TRAVELRULECOMPANYCODE`, `TRAVELRULEITEMTYPE`, `TRLEMPLOYEEGRADEICSTABLECODE`, `TRAVELRULEEMPLOYEEGRADECODE`, `TRAVELRULEEFFECTIVEFROMDATE` | `TRAVELRULEDETAIL.TRAVELRULECOMPANYCODE = TRAVELRULE.COMPANYCODE AND TRAVELRULEDETAIL.TRAVELRULEITEMTYPE = TRAVELRULE.ITEMTYPE AND TRAVELRULEDETAIL.TRLEMPLOYEEGRADEICSTABLECODE = TRAVELRULE.EMPLOYEEGRADEICSTABLECODE AND TRAVELRULEDETAIL.TRAVELRULEEMPLOYEEGRADECODE = TRAVELRULE.EMPLOYEEGRADECODE AND TRAVELRULEDETAIL.TRAVELRULEEFFECTIVEFROMDATE = TRAVELRULE.EFFECTIVEFROMDATE` |

## Indexes

- `TRAVELRULEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPE,
       t.EMPLOYEEGRADEICSTABLECODE,
       t.EMPLOYEEGRADECODE,
       t.EFFECTIVEFROMDATE,
       t.EFFECTIVETODATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.TRAVELRULE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
