# DB2ADMIN.BUDGETITEMSETUP

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`, `TYPE`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 190054

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `TYPE` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `SUBCODE01CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 5 | `SUBCODE02CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 6 | `SUBCODE03CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 7 | `SUBCODE04CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 8 | `SUBCODE05CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 9 | `SUBCODE06CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `SUBCODE07CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 11 | `SUBCODE08CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `SUBCODE09CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 13 | `SUBCODE10CONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 14 | `BUDGETGROUPCONTROLLED` | SMALLINT | NOT NULL |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 22 | `EXTRAPERCENTAGE` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 23 | `ROUNDUPTONEXTDECIMAL` | SMALLINT | NOT NULL |  |  |  |
| 24 | `NUMBEROFDECIMALSFORROUNDING` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `BUDGETITEMSETUP.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BUDGETITEMSETUP.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND BUDGETITEMSETUP.ITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `BUDGETITEMSETUP_DETAIL` | [`BUDGETITEMSETUPDETAIL`](../OTHER/BUDGETITEMSETUPDETAIL.md) | `BUDGETCOMPANYCODE`, `BUDGETITEMTYPECODE`, `BUDGETITEMSETUPTYPE` | `BUDGETITEMSETUPDETAIL.BUDGETCOMPANYCODE = BUDGETITEMSETUP.COMPANYCODE AND BUDGETITEMSETUPDETAIL.BUDGETITEMTYPECODE = BUDGETITEMSETUP.ITEMTYPECODE AND BUDGETITEMSETUPDETAIL.BUDGETITEMSETUPTYPE = BUDGETITEMSETUP.TYPE` |

## Indexes

- `BUDGETITEMSETUPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.TYPE,
       t.SUBCODE01CONTROLLED,
       t.SUBCODE02CONTROLLED,
       t.SUBCODE03CONTROLLED,
       t.SUBCODE04CONTROLLED,
       t.SUBCODE05CONTROLLED,
       t.SUBCODE06CONTROLLED,
       t.SUBCODE07CONTROLLED,
       t.SUBCODE08CONTROLLED
FROM   DB2ADMIN.BUDGETITEMSETUP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
